import unittest
from models.base_model import BaseModel
from datetime import datetime
import models


class TestBaseModel(unittest.TestCase):

    def setUp(self):
        """Set up  BaseModel testing."""
        self.model = BaseModel()

    def test_init(self):
        """Test the BaseModel instance."""
        self.assertIsInstance(self.model.id, str)
        self.assertIsInstance(self.model.created_at, datetime)
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_str(self):
        """Test the BaseModel str."""
        ex_output = f"[BaseModel] ({self.model.id}) {self.model.__dict__}"
        self.assertEqual(str(self.model), ex_output)

    def test_save(self):
        """Test the BaseModel save."""
        old_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(old_updated_at, self.model.updated_at)

    def test_to_dict(self):
        """Test the BaseModel to_dict."""
        result = self.model.to_dict()
        self.assertIsInstance(result, dict)
        self.assertEqual(result["__class__"], "BaseModel")
        self.assertEqual(result["id"], self.model.id)
        self.assertEqual(result["updated_at"],
                         self.model.updated_at.isoformat())


if __name__ == '__main__':
    unittest.main()
