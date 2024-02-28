#!/usr/bin/python3
"""Unittest for file_storage"""
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models import storage
import json


class TestFileStorage(unittest.TestCase):
    """Class to test file storage module"""
    def setUp(self):
        """Set up test method"""
        self.file_storage_instance = FileStorage()

    def test_all(self):
        """Test all method"""
        self.assertIsInstance(storage.all(), dict)

    def test_new(self):
        """Test new method"""
        obj = BaseModel()
        storage.new(obj)
        self.assertIn("BaseModel." + obj.id, storage.all())

    def test_save(self):
        """Test save method"""
        obj = BaseModel()
        storage.new(obj)
        storage.save()
        with open("file.json", "r") as file:
            file_content = json.load(file)
        self.assertIn("BaseModel." + obj.id, file_content)

    def test_reload(self):
        """Test reload method"""
        obj = BaseModel()
        storage.new(obj)
        storage.save()
        storage.reload()
        self.assertIn("BaseModel." + obj.id, storage.all())

    def test_all_after_reload(self):
        """Test all method after reload"""
        obj = BaseModel()
        storage.new(obj)
        storage.save()
        storage.reload()
        self.assertIsInstance(storage.all(), dict)

    def test_new_after_reload(self):
        """Test new method after reload"""
        obj = BaseModel()
        storage.new(obj)
        storage.save()
        storage.reload()
        self.assertIn("BaseModel." + obj.id, storage.all())

    def test_save_after_reload(self):
        """Test save method after reload"""
        obj = BaseModel()
        storage.new(obj)
        storage.save()
        storage.reload()
        with open("file.json", "r") as file:
            file_content = json.load(file)
        self.assertIn("BaseModel." + obj.id, file_content)

    def test_reload_after_reload(self):
        """Test reload method after reload"""
        obj = BaseModel()
        storage.new(obj)
        storage.save()
        storage.reload()
        storage.reload()
        self.assertIn("BaseModel." + obj.id, storage.all())


if __name__ == "__main__":
    unittest.main()
