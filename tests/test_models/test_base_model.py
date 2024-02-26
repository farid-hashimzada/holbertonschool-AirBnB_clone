#!/usr/bin/python3
"""Unittest for base model"""
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Class to test base model module"""
    def test_base(self):
        """Test base case"""
        base_instance = BaseModel()
        self.assertIsInstance(base_instance, BaseModel)
        self.assertEqual(base_instance.__class__.__name__, "BaseModel")

    def test_str(self):
        """str method case"""
        base_instance = BaseModel()
        base_instance.name = "My First Model"
        base_instance.my_number = 89
        self.assertEqual(str(base_instance),
                         f"[{base_instance.__class__.__name__}]
                         ({base_instance.id}) {base_instance.__dict__}")

    def test_save(self):
        """save method case"""
        base_instance = BaseModel()
        base_instance.save()
        self.assertNotEqual(base_instance.created_at, base_instance.updated_at)

    def test_to_dict(self):
        """to_dict method case"""
        base_instance = BaseModel()
        base_instance_dict = base_instance.to_dict()
        self.assertEqual(base_instance_dict["__class__"], "BaseModel")
        self.assertEqual(base_instance_dict["id"], base_instance.id)
        self.assertEqual(base_instance_dict["created_at"],
                         base_instance.created_at.isoformat())
        self.assertEqual(base_instance_dict["updated_at"],
                         base_instance.updated_at.isoformat())


if __name__ == "__main__":
    unittest.main()
