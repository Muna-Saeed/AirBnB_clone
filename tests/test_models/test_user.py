#!/usr/bin/python3
"""Test cases for User class."""
import unittest
from datetime import datetime
from models.user import User


class TestUser(unittest.TestCase):
    """Test cases for User class."""

    def setUp(self):
        """Set up for testing."""
        self.user = User()

    def test_inheritance(self):
        """Test if User inherits from BaseModel."""
        self.assertIsInstance(self.user, BaseModel)

    def test_attributes(self):
        """Test User attributes."""
        self.assertTrue(hasattr(self.user, 'email'))
        self.assertTrue(hasattr(self.user, 'password'))
        self.assertTrue(hasattr(self.user, 'first_name'))
        self.assertTrue(hasattr(self.user, 'last_name'))

    def test_attribute_types(self):
        """Test User attribute types."""
        self.assertIsInstance(self.user.email, str)
        self.assertIsInstance(self.user.password, str)
        self.assertIsInstance(self.user.first_name, str)
        self.assertIsInstance(self.user.last_name, str)

    def test_empty_strings(self):
        """Test if User attributes are initialized as empty strings."""
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")

    def test_to_dict_method(self):
        """Test the to_dict method of User."""
        user_dict = self.user.to_dict()
        self.assertEqual(user_dict['email'], self.user.email)
        self.assertEqual(user_dict['password'], self.user.password)
        self.assertEqual(user_dict['first_name'], self.user.first_name)
        self.assertEqual(user_dict['last_name'], self.user.last_name)
        self.assertEqual(user_dict['__class__'], 'User')

    def test_to_dict_method_with_datetime(self):
        """Test the to_dict method with datetime attributes."""
        self.user.created_at = datetime(2022, 1, 1, 12, 0, 0)
        self.user.updated_at = datetime(2022, 1, 2, 12, 0, 0)
        user_dict = self.user.to_dict()
        self.assertEqual(user_dict['created_at'], '2022-01-01T12:00:00')
        self.assertEqual(user_dict['updated_at'], '2022-01-02T12:00:00')

if __name__ == "__main__":
    unittest.main()
