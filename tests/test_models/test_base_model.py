#!/usr/bin/python3
"""Module for testing BaseModel class."""
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class."""

    def test_attributes(self):
        """Test the public instance attributes."""
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89
        self.assertEqual(type(my_model.id), str)
        self.assertEqual(type(my_model.created_at), datetime)
        self.assertEqual(type(my_model.updated_at), datetime)

    def test_str_method(self):
        """Test the __str__ method."""
        my = BaseModel()
        my.name = "My First Model"
        my.my_number = 89
        expected_str = "[BaseModel] ({}) {}".format(my.id, my.__dict__)
        self.assertEqual(str(my), expected_str)

    def test_save_method(self):
        """Test the save method."""
        my_model = BaseModel()
        prev_updated_at = my_model.updated_at
        my_model.save()
        self.assertNotEqual(prev_updated_at, my_model.updated_at)

    def test_to_dict_method(self):
        """Test the to_dict method."""
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89
        my_model_json = my_model.to_dict()
        self.assertEqual(type(my_model_json['created_at']), str)
        self.assertEqual(type(my_model_json['updated_at']), str)
        self.assertEqual(type(my_model_json['__class__']), str)
        self.assertEqual(my_model_json['__class__'], 'BaseModel')

    def test_init_method(self):
        """Test the __init__ method."""
        # Test default initialization
        my_model_default = BaseModel()
        self.assertIsInstance(my_model_default.id, str)
        self.assertIsInstance(my_model_default.created_at, datetime)
        self.assertIsInstance(my_model_default.updated_at, datetime)

        # Test initialization with specific values
        specific_created_at = datetime(2022, 1, 1, 12, 0, 0)
        specific_updated_at = datetime(2022, 1, 2, 12, 0, 0)
        my_model_specific = BaseModel(
            created_at=specific_created_at, updated_at=specific_updated_at
        )
        self.assertEqual(my_model_specific.created_at, specific_created_at)
        self.assertEqual(my_model_specific.updated_at, specific_updated_at)

    def test_set_attr_method(self):
        """Test the set_attr method."""
        my_model = BaseModel()
        my_model.set_attr(name="My Model", my_number=42)
        self.assertEqual(my_model.name, "My Model")
        self.assertEqual(my_model.my_number, 42)

    def test_update_method(self):
        """Test the update method."""
        my_model = BaseModel()
        my_model.update("name", "Updated Model")
        self.assertEqual(my_model.name, "Updated Model")

    def test_destroy_method(self):
        """Test the destroy method."""
        my_model = BaseModel()
        obj_id = my_model.id
        BaseModel.destroy(obj_id)
        self.assertIsNone(BaseModel.get_object(obj_id))

if __name__ == "__main__":
    unittest.main()
