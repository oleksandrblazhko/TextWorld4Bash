# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT license.

import os
import json
from typing import Tuple, Optional

import textworld
from textworld.core import EnvInfos, GameState, Wrapper


class BashCommandMappingWrapper(Wrapper):
    """
    Wrapper to translate TextWorld commands to Bash-like commands (e.g. ls, cd)
    using the mapping from tw_bash_command_mapping.json.
    This version supports commands with arguments using '{}' as a placeholder.
    """

    def __init__(self, env: textworld.Environment, mapping_path: Optional[str] = None) -> None:
        super().__init__(env)
        self.bash_to_tw = {}
        self.tw_to_bash = {}
        
        if mapping_path is None:
            # Locate relative to the package directory as a fallback
            package_dir = os.path.dirname(os.path.abspath(textworld.__file__))
            mapping_path = os.path.join(package_dir, "..", "Research", "prompts", "tw_bash_command_mapping.json")

        self.mapping_path = os.path.abspath(mapping_path)
        self._load_mappings()

    def _load_mappings(self):
        if not os.path.exists(self.mapping_path):
            return

        try:
            with open(self.mapping_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            for item in data.get("commands", []):
                tw_cmd = item["tw"].strip().lower()
                bash_cmd = item["bash"].strip().lower()
                self.bash_to_tw[bash_cmd] = tw_cmd
                self.tw_to_bash[tw_cmd] = bash_cmd
        except Exception as e:
            pass

    def _translate_command(self, command: str, mapping_dict: dict) -> str:
        cmd_lower = command.strip().lower()

        # First, try for an exact match (for commands without arguments).
        if cmd_lower in mapping_dict:
            return mapping_dict[cmd_lower]

        # Then, try to match commands with arguments.
        for from_template, to_template in mapping_dict.items():
            if "{}" in from_template:
                parts = from_template.split("{}", 1)
                prefix = parts[0]
                suffix = parts[1]

                if cmd_lower.startswith(prefix) and cmd_lower.endswith(suffix):
                    # Extract argument from the middle.
                    start = len(prefix)
                    end = len(cmd_lower) - len(suffix)
                    arg = cmd_lower[start:end].strip()
                    
                    if arg:
                        return to_template.replace("{}", arg, 1)

        return command  # Return original if no match found.

    def _translate_state(self, state: GameState) -> GameState:
        if state is None:
            return state

        # Translate admissible commands
        if "admissible_commands" in state and state["admissible_commands"]:
            state["admissible_commands"] = [self._translate_command(cmd, self.tw_to_bash) for cmd in state["admissible_commands"]]

        # Translate policy commands
        if "policy_commands" in state and state["policy_commands"]:
            state["policy_commands"] = [self._translate_command(cmd, self.tw_to_bash) for cmd in state["policy_commands"]]

        # Translate last command
        if "last_command" in state and state["last_command"]:
            state["last_command"] = self._translate_command(state["last_command"], self.tw_to_bash)

        return state

    def step(self, command: str) -> Tuple[GameState, float, bool]:
        # Translate incoming command from Bash to TW
        tw_command = self._translate_command(command, self.bash_to_tw)

        # Call the underlying environment step
        state, reward, done = self._wrapped_env.step(tw_command)

        # Translate output state back to Bash format
        state = self._translate_state(state)
        return state, reward, done

    def reset(self) -> GameState:
        state = self._wrapped_env.reset()
        state = self._translate_state(state)
        return state

    def copy(self) -> "BashCommandMappingWrapper":
        env_copy = self._wrapped_env.copy()
        wrapper_copy = BashCommandMappingWrapper(env_copy, self.mapping_path)
        wrapper_copy.bash_to_tw = dict(self.bash_to_tw)
        wrapper_copy.tw_to_bash = dict(self.tw_to_bash)
        return wrapper_copy
