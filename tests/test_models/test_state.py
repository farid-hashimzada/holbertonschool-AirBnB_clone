#!/usr/bin/python3
"""Unittest for state"""
import unittest
from models.state import State


class TestState(unittest.TestCase):
    """Class to test state module"""
    def test_state(self):
        """Test state class"""
        state_instance = State()
        self.assertIsInstance(state_instance, State)
        self.assertEqual(state_instance.__class__.__name__, "State")

    def test_state_name(self):
        """Test state name attribute"""
        state_instance = State()
        self.assertEqual(state_instance.name, "")

    def test_state_name_assignment(self):
        """Test state name assignment"""
        state_instance = State()
        state_instance.name = "California"
        self.assertEqual(state_instance.name, "California")


if __name__ == "__main__":
    unittest.main()
