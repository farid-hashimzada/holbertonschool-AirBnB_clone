#!/usr/bin/python3
"""Unittest for base model"""
import unittest
from models.base_model import Base


class TestBaseModel(unittest.TestCase):
    """Class to test base model module"""
    def test_base(self):
        """Test base class"""
        base_instance = Base()
        self.assertIsInstance(base_instance, Base)
        self.assertEqual(base_instance.__class__.__name__, "Base")


if __name__ == "__main__":
    unittest.main()
