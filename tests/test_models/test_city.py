#!/usr/bin/python3
"""Unittest for city"""
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """Class to test city module"""
    def test_city(self):
        """Test city class"""
        city_instance = City()
        self.assertIsInstance(city_instance, City)
        self.assertEqual(city_instance.__class__.__name__, "City")


if __name__ == "__main__":
    unittest.main()
