#!/usr/bin/env python3
"""Test cases for Amenity class."""
import unittest
from datetime import datetime
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Test cases for Amenity class."""

    def setUp(self):
        """Set up for testing."""
        self.amenity = Amenity()

    def test_inheritance(self):
        """Test if Amenity inherits from BaseModel."""
        self.assertIsInstance(self.amenity, BaseModel)

    def test_attributes(self):
        """Test Amenity attributes."""
        self.assertTrue(hasattr(self.amenity, 'name'))

    def test_attribute_types(self):
        """Test Amenity attribute types."""
        self.assertIsInstance(self.amenity.name, str)

    def test_empty_string(self):
        """Test if Amenity attribute is initialized as an empty string."""
        self.assertEqual(self.amenity.name, "")

    def test_to_dict_method(self):
        """Test the to_dict method of Amenity."""
        amenity_dict = self.amenity.to_dict()
        self.assertEqual(amenity_dict['name'], self.amenity.name)
        self.assertEqual(amenity_dict['__class__'], 'Amenity')

    def test_to_dict_method_with_datetime(self):
        """Test the to_dict method with datetime attributes."""
        self.amenity.created_at = datetime(2022, 1, 1, 12, 0, 0)
        self.amenity.updated_at = datetime(2022, 1, 2, 12, 0, 0)
        amenity_dict = self.amenity.to_dict()
        self.assertEqual(amenity_dict['created_at'], '2022-01-01T12:00:00')
        self.assertEqual(amenity_dict['updated_at'], '2022-01-02T12:00:00')

if __name__ == "__main__":
    unittest.main()
