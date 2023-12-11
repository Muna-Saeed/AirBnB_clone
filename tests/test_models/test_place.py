#!/usr/bin/env python3
"""Test cases for Place class."""
import unittest
from datetime import datetime
from models.place import Place


class TestPlace(unittest.TestCase):
    """Test cases for Place class."""

    def setUp(self):
        """Set up for testing."""
        self.place = Place()

    def test_inheritance(self):
        """Test if Place inherits from BaseModel."""
        self.assertIsInstance(self.place, BaseModel)

    def test_attributes(self):
        """Test Place attributes."""
        self.assertTrue(hasattr(self.place, 'city_id'))
        self.assertTrue(hasattr(self.place, 'user_id'))
        self.assertTrue(hasattr(self.place, 'name'))
        self.assertTrue(hasattr(self.place, 'description'))
        self.assertTrue(hasattr(self.place, 'number_rooms'))
        self.assertTrue(hasattr(self.place, 'number_bathrooms'))
        self.assertTrue(hasattr(self.place, 'max_guest'))
        self.assertTrue(hasattr(self.place, 'price_by_night'))
        self.assertTrue(hasattr(self.place, 'latitude'))
        self.assertTrue(hasattr(self.place, 'longitude'))
        self.assertTrue(hasattr(self.place, 'amenity_ids'))

    def test_attribute_types(self):
        """Test Place attribute types."""
        self.assertIsInstance(self.place.city_id, str)
        self.assertIsInstance(self.place.user_id, str)
        self.assertIsInstance(self.place.name, str)
        self.assertIsInstance(self.place.description, str)
        self.assertIsInstance(self.place.number_rooms, int)
        self.assertIsInstance(self.place.number_bathrooms, int)
        self.assertIsInstance(self.place.max_guest, int)
        self.assertIsInstance(self.place.price_by_night, int)
        self.assertIsInstance(self.place.latitude, float)
        self.assertIsInstance(self.place.longitude, float)
        self.assertIsInstance(self.place.amenity_ids, list)

    def test_default_values(self):
        """Test default values of attributes."""
        self.assertEqual(self.place.city_id, "")
        self.assertEqual(self.place.user_id, "")
        self.assertEqual(self.place.name, "")
        self.assertEqual(self.place.description, "")
        self.assertEqual(self.place.number_rooms, 0)
        self.assertEqual(self.place.number_bathrooms, 0)
        self.assertEqual(self.place.max_guest, 0)
        self.assertEqual(self.place.price_by_night, 0)
        self.assertEqual(self.place.latitude, 0.0)
        self.assertEqual(self.place.longitude, 0.0)
        self.assertEqual(self.place.amenity_ids, [])

    def test_to_dict_method(self):
        """Test the to_dict method of Place."""
        place_dict = self.place.to_dict()
        self.assertEqual(place_dict['city_id'], self.place.city_id)
        self.assertEqual(place_dict['user_id'], self.place.user_id)
        self.assertEqual(place_dict['name'], self.place.name)
        self.assertEqual(place_dict['description'], self.place.description)
        self.assertEqual(place_dict['number_rooms'], self.place.number_rooms)
        self.assertEqual(place_dict['number_bathrooms'], self.place.number_bathrooms)
        self.assertEqual(place_dict['max_guest'], self.place.max_guest)
        self.assertEqual(place_dict['price_by_night'], self.place.price_by_night)
        self.assertEqual(place_dict['latitude'], self.place.latitude)
        self.assertEqual(place_dict['longitude'], self.place.longitude)
        self.assertEqual(place_dict['amenity_ids'], self.place.amenity_ids)
        self.assertEqual(place_dict['__class__'], 'Place')

    def test_to_dict_method_with_datetime(self):
        """Test the to_dict method with datetime attributes."""
        self.place.created_at = datetime(2022, 1, 1, 12, 0, 0)
        self.place.updated_at = datetime(2022, 1, 2, 12, 0, 0)
        place_dict = self.place.to_dict()
        self.assertEqual(place_dict['created_at'], '2022-01-01T12:00:00')
        self.assertEqual(place_dict['updated_at'], '2022-01-02T12:00:00')

if __name__ == "__main__":
    unittest.main()
