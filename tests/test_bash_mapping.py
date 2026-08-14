# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT license.

import os
import unittest

import textworld
from textworld.core import GameState
from textworld.envs.wrappers.bash_mapping import BashCommandMappingWrapper


class DummyEnvironment(textworld.Environment):
    def __init__(self):
        super().__init__()
        self.state = GameState()
        self.state["admissible_commands"] = ["look", "go north", "go south", "take key"]
        self.state["policy_commands"] = ["go north", "look"]
        self.state["last_command"] = None
        self.received_commands = []

    def step(self, command: str):
        self.received_commands.append(command)
        state_copy = self.state.copy()
        state_copy["last_command"] = command
        return state_copy, 0.0, False

    def reset(self):
        self.received_commands = []
        self.state["last_command"] = None
        return self.state.copy()


class TestBashMapping(unittest.TestCase):

    def test_wrapper_mapping(self):
        # Create a dummy environment
        dummy_env = DummyEnvironment()
        
        # Wrap it using our mapping wrapper
        wrapped_env = BashCommandMappingWrapper(dummy_env)
        
        # Test reset: should translate admissible_commands and policy_commands
        state = wrapped_env.reset()
        self.assertIn("ls", state["admissible_commands"])
        self.assertIn("cd north", state["admissible_commands"])
        self.assertNotIn("go south", state["admissible_commands"])  # "go south" -> "cd south"
        self.assertIn("cd south", state["admissible_commands"])
        self.assertIn("take key", state["admissible_commands"])  # Not in mapping, should remain as is
        self.assertNotIn("look", state["admissible_commands"])
        self.assertNotIn("go north", state["admissible_commands"])

        # Test policy command translation
        self.assertIn("cd north", state["policy_commands"])
        self.assertNotIn("go north", state["policy_commands"])

        # Test step: user inputs bash command, underlying environment should receive TW command
        state, reward, done = wrapped_env.step("ls")
        
        # Under the hood, dummy_env should have received "look"
        self.assertIn("look", dummy_env.received_commands)
        
        # The returned state should show the bash command as last_command
        self.assertEqual(state["last_command"], "ls")

        # Test step with unmapped command: should pass through
        state, reward, done = wrapped_env.step("take key")
        self.assertIn("take key", dummy_env.received_commands)
        self.assertEqual(state["last_command"], "take key")


if __name__ == "__main__":
    unittest.main()
