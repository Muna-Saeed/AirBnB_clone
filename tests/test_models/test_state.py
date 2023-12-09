#!/usr/bin/env python3
"""Test cases for State class."""
import unittest
from datetime import datetime
from models.state import State


class TestState(unittest.TestCase):
    """Test cases for State class."""

    def setUp(self):
        """Set up for testing."""
        self.state = State()

    def test_inheritance(self):
        """Test if State inherits from BaseModel."""
        self.assertIsInstance(self.state, BaseModel)

    def test_attributes(self):
        """Test State attributes."""
        self.assertTrue(hasattr(self.state, 'name'))

    def test_attribute_types(self):
        """Test State attribute types."""
        self.assertIsInstance(self.state.name, str)

    def test_empty_string(self):
        """Test if State attribute is initialized as an empty string."""
        self.assertEqual(self.state.name, "")

    def test_to_dict_method(self):
        """Test the to_dict method of State."""
        state_dict = self.state.to_dict()
        self.assertEqual(state_dict['name'], self.state.name)
        self.assertEqual(state_dict['__class__'], 'State')

    def test_to_dict_method_with_datetime(self):
        """Test the to_dict method with datetime attributes."""
        self.state.created_at = datetime(2022, 1, 1, 12, 0, 0)
        self.state.updated_at = datetime(2022, 1, 2, 12, 0, 0)
        state_dict = self.state.to_dict()
        self.assertEqual(state_dict['created_at'], '2022-01-01T12:00:00')
        self.assertEqual(state_dict['updated_at'], '2022-01-02T12:00:00')

if __name__ == "__main__":
    unittest.main()
