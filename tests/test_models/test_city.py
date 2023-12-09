#!/usr/bin/env python3
"""Test cases for City class."""
import unittest
from datetime import datetime
from models.city import City


class TestCity(unittest.TestCase):
    """Test cases for City class."""

    def setUp(self):
        """Set up for testing."""
        self.city = City()

    def test_inheritance(self):
        """Test if City inherits from BaseModel."""
        self.assertIsInstance(self.city, BaseModel)

    def test_attributes(self):
        """Test City attributes."""
        self.assertTrue(hasattr(self.city, 'state_id'))
        self.assertTrue(hasattr(self.city, 'name'))

    def test_attribute_types(self):
        """Test City attribute types."""
        self.assertIsInstance(self.city.state_id, str)
        self.assertIsInstance(self.city.name, str)

    def test_empty_strings(self):
        """Test if City attributes are initialized as empty strings."""
        self.assertEqual(self.city.state_id, "")
        self.assertEqual(self.city.name, "")

    def test_to_dict_method(self):
        """Test the to_dict method of City."""
        city_dict = self.city.to_dict()
        self.assertEqual(city_dict['state_id'], self.city.state_id)
        self.assertEqual(city_dict['name'], self.city.name)
        self.assertEqual(city_dict['__class__'], 'City')

    def test_to_dict_method_with_datetime(self):
        """Test the to_dict method with datetime attributes."""
        self.city.created_at = datetime(2022, 1, 1, 12, 0, 0)
        self.city.updated_at = datetime(2022, 1, 2, 12, 0, 0)
        city_dict = self.city.to_dict()
        self.assertEqual(city_dict['created_at'], '2022-01-01T12:00:00')
        self.assertEqual(city_dict['updated_at'], '2022-01-02T12:00:00')

if __name__ == "__main__":
    unittest.main()
