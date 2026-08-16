# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT license.

import os
import re
import json
from typing import Tuple, Optional, List, Dict

import textworld
from textworld.core import EnvInfos, GameState, Wrapper


class BashCommandMappingWrapper(Wrapper):
    """
    Wrapper to translate TextWorld commands to Bash-like commands and vice-versa.
    This version supports commands with single ('{}') and multiple ('{1}', '{2}')
    arguments using regular expressions.
    """

    def __init__(self, env: textworld.Environment, mapping_path: Optional[str] = None) -> None:
        super().__init__(env)
        self.bash_to_tw_mappings = []
        self.tw_to_bash_mappings = []
        
        if mapping_path is None:
            package_dir = os.path.dirname(os.path.abspath(textworld.__file__))
            mapping_path = os.path.join(package_dir, "..", "scripts", "tw_bash_command_mapping.json")

        self.mapping_path = os.path.abspath(mapping_path)
        self._load_mappings()

    def _load_mappings(self):
        if not os.path.exists(self.mapping_path):
            return

        try:
            with open(self.mapping_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            for item in data.get("commands", []):
                bash_template = item["bash"]
                tw_template = item["tw"]

                # Bash -> TW mapping
                self.bash_to_tw_mappings.append(self._create_mapping_entry(bash_template, tw_template))
                
                # TW -> Bash mapping
                self.tw_to_bash_mappings.append(self._create_mapping_entry(tw_template, bash_template))
        except Exception as e:
            # You might want to log this error.
            pass
            
    def _create_mapping_entry(self, from_template: str, to_template: str) -> Dict:
        """Converts a template string into a regex for parsing arguments."""
        # Find all placeholders like {1}, {2}, {}
        placeholders = re.findall(r'(\{\d*?\})', from_template)
        
        # Build regex pattern by replacing placeholders with capture groups
        # We use (.+) which is greedy. For many cases, (\\S+) might be safer.
        regex_pattern = re.escape(from_template)
        for placeholder in sorted(placeholders, key=len, reverse=True):
            regex_pattern = regex_pattern.replace(re.escape(placeholder), r'(.+)')
            
        return {
            "regex": re.compile(f"^{regex_pattern}$", re.IGNORECASE),
            "template": to_template,
            "placeholders": placeholders
        }

    def _translate_command(self, command: str, mappings: List[Dict]) -> str:
        command = command.strip()
        for entry in mappings:
            match = entry["regex"].match(command)
            if match:
                output = entry["template"]
                args = match.groups()
                
                if not entry["placeholders"] or not args:
                    return output # No argument substitution needed

                # Substitute numbered placeholders {1}, {2}, etc.
                if entry["placeholders"][0].startswith('{1'):
                    for i, arg in enumerate(args):
                        output = output.replace(f'{{{i+1}}}', arg)
                # Substitute single placeholder {}
                elif args:
                    output = output.replace('{}', args[0])
                
                return output

        return command

    def _translate_state(self, state: GameState) -> GameState:
        if state is None:
            return state

        if "admissible_commands" in state and state["admissible_commands"]:
            state["admissible_commands"] = [self._translate_command(cmd, self.tw_to_bash_mappings) for cmd in state["admissible_commands"]]

        if "policy_commands" in state and state["policy_commands"]:
            state["policy_commands"] = [self._translate_command(cmd, self.tw_to_bash_mappings) for cmd in state["policy_commands"]]

        if "last_command" in state and state["last_command"]:
            state["last_command"] = self._translate_command(state["last_command"], self.tw_to_bash_mappings)

        return state

    def step(self, command: str) -> Tuple[GameState, float, bool]:
        tw_command = self._translate_command(command, self.bash_to_tw_mappings)
        state, reward, done = self._wrapped_env.step(tw_command)
        state = self._translate_state(state)
        return state, reward, done

    def reset(self) -> GameState:
        state = self._wrapped_env.reset()
        state = self._translate_state(state)
        return state

    def copy(self) -> "BashCommandMappingWrapper":
        env_copy = self._wrapped_env.copy()
        wrapper_copy = BashCommandMappingWrapper(env_copy, self.mapping_path)
        # Re-creating mappings is safer than deep copying regex
        wrapper_copy._load_mappings() 
        return wrapper_copy
