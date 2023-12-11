#!/usr/bin/env python3
"""Test cases for Review class."""
import unittest
from datetime import datetime
from models.review import Review


class TestReview(unittest.TestCase):
    """Test cases for Review class."""

    def setUp(self):
        """Set up for testing."""
        self.review = Review()

    def test_inheritance(self):
        """Test if Review inherits from BaseModel."""
        self.assertIsInstance(self.review, BaseModel)

    def test_attributes(self):
        """Test Review attributes."""
        self.assertTrue(hasattr(self.review, 'place_id'))
        self.assertTrue(hasattr(self.review, 'user_id'))
        self.assertTrue(hasattr(self.review, 'text'))

    def test_attribute_types(self):
        """Test Review attribute types."""
        self.assertIsInstance(self.review.place_id, str)
        self.assertIsInstance(self.review.user_id, str)
        self.assertIsInstance(self.review.text, str)

    def test_empty_strings(self):
        """Test if Review attributes are initialized as empty strings."""
        self.assertEqual(self.review.place_id, "")
        self.assertEqual(self.review.user_id, "")
        self.assertEqual(self.review.text, "")

    def test_to_dict_method(self):
        """Test the to_dict method of Review."""
        review_dict = self.review.to_dict()
        self.assertEqual(review_dict['place_id'], self.review.place_id)
        self.assertEqual(review_dict['user_id'], self.review.user_id)
        self.assertEqual(review_dict['text'], self.review.text)
        self.assertEqual(review_dict['__class__'], 'Review')

    def test_to_dict_method_with_datetime(self):
        """Test the to_dict method with datetime attributes."""
        self.review.created_at = datetime(2022, 1, 1, 12, 0, 0)
        self.review.updated_at = datetime(2022, 1, 2, 12, 0, 0)
        review_dict = self.review.to_dict()
        self.assertEqual(review_dict['created_at'], '2022-01-01T12:00:00')
        self.assertEqual(review_dict['updated_at'], '2022-01-02T12:00:00')

if __name__ == "__main__":
    unittest.main()
