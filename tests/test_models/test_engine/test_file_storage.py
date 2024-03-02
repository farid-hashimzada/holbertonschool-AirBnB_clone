import unittest
from models.base_model import BaseModel
from models import storage
import os


class TestFileStorage(unittest.TestCase):
    """Test the FileStorage class"""

    def setUp(self):
        """Set up the tests."""
        try:
            os.remove('file.json')
        except IOError:
            pass

        storage.__objects = {}

    def test_all(self):
        """Test the all method."""
        new_model = BaseModel()
        storage.new(new_model)
        self.assertIn('BaseModel.' + new_model.id, storage.all())

    def test_new(self):
        """Test the new method."""
        new_model = BaseModel()
        storage.new(new_model)
        self.assertIn('BaseModel.' + new_model.id, storage.all())

    def test_save(self):
        """Test the save method."""
        new_model = BaseModel()
        storage.new(new_model)
        storage.save()
        with open('file.json', 'r') as file:
            self.assertIn('BaseModel.' + new_model.id, file.read())

    def test_reload(self):
        """Test the reload method."""
        new_md = BaseModel()
        storage.save()
        storage.objects = {}
        storage.reload()
        self.assertIn('BaseModel.' + new_md.id, storage.all())


if __name__ == '__main__':
    unittest.main()
