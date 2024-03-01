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

    def test_place_attributes(self):
        """Test place attributes"""
        place_instance = Place()
        self.assertEqual(place_instance.city_id, "")
        self.assertEqual(place_instance.user_id, "")
        self.assertEqual(place_instance.name, "")
        self.assertEqual(place_instance.description, "")
        self.assertEqual(place_instance.number_rooms, 0)
        self.assertEqual(place_instance.number_bathrooms, 0)
        self.assertEqual(place_instance.max_guest, 0)
        self.assertEqual(place_instance.price_by_night, 0)
        self.assertEqual(place_instance.latitude, 0.0)
        self.assertEqual(place_instance.longitude, 0.0)
        self.assertEqual(place_instance.amenity_ids, [])


if __name__ == "__main__":
    unittest.main()
