#!/usr/bin/python3
"""Unittest for amenity"""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Class to test amenity module"""
    def test_amenity(self):
        """Test amenity class"""
        amenity_instance = Amenity()
        self.assertIsInstance(amenity_instance, Amenity)
        self.assertEqual(amenity_instance.__class__.__name__, "Amenity")

    def test_amenity_name(self):
        """Test amenity name attribute"""
        amenity_instance = Amenity()
        self.assertEqual(amenity_instance.name, "")


if __name__ == "__main__":
    unittest.main()
