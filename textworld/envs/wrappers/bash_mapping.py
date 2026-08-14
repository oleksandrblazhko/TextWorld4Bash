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
            # Fallback if file not found (e.g. if run outside repository context)
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
            # Fail silently or log error if necessary
            pass

    def _translate_state(self, state: GameState) -> GameState:
        if state is None:
            return state

        # Translate admissible commands
        if "admissible_commands" in state and state["admissible_commands"]:
            translated_commands = []
            for cmd in state["admissible_commands"]:
                cmd_lower = cmd.strip().lower()
                # Check for exact matches
                if cmd_lower in self.tw_to_bash:
                    translated_commands.append(self.tw_to_bash[cmd_lower])
                else:
                    translated_commands.append(cmd)
            state["admissible_commands"] = translated_commands

        # Translate policy commands (oracle suggestions)
        if "policy_commands" in state and state["policy_commands"]:
            translated_policy = []
            for cmd in state["policy_commands"]:
                cmd_lower = cmd.strip().lower()
                if cmd_lower in self.tw_to_bash:
                    translated_policy.append(self.tw_to_bash[cmd_lower])
                else:
                    translated_policy.append(cmd)
            state["policy_commands"] = translated_policy

        # Translate last command
        if "last_command" in state and state["last_command"]:
            cmd_lower = state["last_command"].strip().lower()
            if cmd_lower in self.tw_to_bash:
                state["last_command"] = self.tw_to_bash[cmd_lower]

        return state

    def step(self, command: str) -> Tuple[GameState, float, bool]:
        # Translate incoming command from Bash to TW
        cmd_stripped = command.strip().lower()
        tw_command = self.bash_to_tw.get(cmd_stripped, command)

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
