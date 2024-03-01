#!/usr/bin/python3
"""Unittest for file_storage"""
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.amenity import Amenity
from models import storage
import os


class TestFileStorage(unittest.TestCase):
    """Class to test file storage module"""
    def setUp(self):
        try:
            os.remove("file.json")
        except IOError:
            pass

    def test_all(self):
        """Test all method"""
        storage = FileStorage()
        new_storage = storage.all()
        self.assertIsInstance(new_storage, dict)

    def test_new(self):
        """Test new method"""
        obj = BaseModel()
        storage = FileStorage()
        storage.new(obj)
        self.assertIn(obj, storage.all().values())

    def test_save(self):
        """Test save method"""
        obj = BaseModel()
        storage = FileStorage()
        storage.new(obj)
        storage.save()
        with open("file.json", "r") as file:
            self.assertIn("BaseModel." + obj.id, file.read())

    def test_reload(self):
        """Tests for reload method"""
        storage = FileStorage()
        new_base = BaseModel()
        new_amenity = Amenity()
        storage.new(new_base)
        storage.new(new_amenity)
        old_objects = storage.all().copy()
        storage.reload()
        for key, obj in storage.all().items():
            self.assertEqual(obj.to_dict(), old_objects[key].to_dict())


if __name__ == "__main__":
    unittest.main()
