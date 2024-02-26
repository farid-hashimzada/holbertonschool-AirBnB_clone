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


if __name__ == "__main__":
    unittest.main()
