#!/usr/bin/python3
"""Unittest for user"""
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """Class to test user module"""
    def test_user(self):
        """Test user class"""
        user_instance = User()
        self.assertIsInstance(user_instance, User)
        self.assertEqual(user_instance.__class__.__name__, "User")

    def test_user_attributes(self):
        """Test user attributes"""
        user_instance = User()
        self.assertEqual(user_instance.email, "")
        self.assertEqual(user_instance.password, "")
        self.assertEqual(user_instance.first_name, "")
        self.assertEqual(user_instance.last_name, "")


if __name__ == "__main__":
    unittest.main()
