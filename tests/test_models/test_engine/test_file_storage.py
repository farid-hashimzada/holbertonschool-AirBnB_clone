import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """Test the FileStorage class"""
    def setUp(self):
        self.storage = FileStorage()

    def test_all(self):
        self.assertIsInstance(self.storage.all(), dict)

    def test_new(self):
        obj = BaseModel()
        self.storage.new(obj)
        self.assertIn('BaseModel.' + obj.id, self.storage.all())

    def test_save(self):
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        with open('file.json', 'r') as f:
            self.assertIn('BaseModel.' + obj.id, f.read())

    def test_reload(self):
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        self.storage.reload()
        self.assertIn('BaseModel.' + obj.id, self.storage.all())


if __name__ == '__main__':
    unittest.main()
