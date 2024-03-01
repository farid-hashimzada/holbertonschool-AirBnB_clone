import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """Test the FileStorage class"""
    def setUp(self):
        self.storage = FileStorage()

    def test_all(self):
        """Test the all method."""
        self.assertIsInstance(self.storage.all(), dict)

    def test_new(self):
        """Test the new method."""
        obj = BaseModel()
        self.storage.new(obj)
        self.assertIn('BaseModel.' + obj.id, self.storage.all())

    def test_save(self):
        """Test the save method."""
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        with open('file.json', 'r') as f:
            self.assertIn('BaseModel.' + obj.id, f.read())

    def test_reload(self):
        """Test the reload method."""
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        self.storage.reload()
        self.assertIn('BaseModel.' + obj.id, self.storage.all())

    def test_reload_no_file(self):
        """Test the reload method with no file."""
        self.storage.reload()
        self.assertIsInstance(self.storage.all(), dict)


if __name__ == '__main__':
    unittest.main()
