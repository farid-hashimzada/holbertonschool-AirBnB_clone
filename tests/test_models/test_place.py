#!/usr/bin/python3
"""Unittest for place"""
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """Class to test place module"""
    def test_place(self):
        """Test place class"""
        place_instance = Place()
        self.assertIsInstance(place_instance, Place)
        self.assertEqual(place_instance.__class__.__name__, "Place")


if __name__ == "__main__":
    unittest.main()
