#!/usr/bin/python3
"""Unittest for file_storage"""
import unittest
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Class to test file storage module"""
    def test_file_storage(self):
        """Test file storage class"""
        file_storage_instance = FileStorage()
        self.assertIsInstance(file_storage_instance, FileStorage)


if __name__ == "__main__":
    unittest.main()
