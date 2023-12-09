#!/usr/bin/python3
"""Test cases for FileStorage class."""
import unittest
from datetime import datetime
from unittest.mock import patch
from io import StringIO
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Test cases for FileStorage class."""

    def setUp(self):
        """Set up for testing."""
        self.file_path = "file.json"
        self.storage = FileStorage()
        self.storage._file_path = self.file_path
        self.model = BaseModel()
        self.user = User()
        self.state = State()
        self.city = City()
        self.amenity = Amenity()
        self.place = Place()
        self.review = Review()

    def tearDown(self):
        """Tear down after testing."""
        try:
            with open(self.file_path, 'w') as f:
                f.write('')
        except FileNotFoundError:
            pass

    def test_destroy_object(self):
        """Test destroy_object method."""
        key = f"{type(self.model).__name__}.{self.model.id}"
        self.storage._objects[key] = self.model
        self.storage.destroy_object(self.model)
        self.assertNotIn(key, self.storage._objects)

    def test_all(self):
        """Test all method."""
        self.assertIsInstance(self.storage.all(), dict)

    def test_new(self):
        """Test new method."""
        key = f"{type(self.model).__name__}.{self.model.id}"
        self.storage.new(self.model)
        self.assertIn(key, self.storage._objects)

    def test_save(self):
        """Test save method."""
        key = f"{type(self.model).__name__}.{self.model.id}"
        self.storage._objects[key] = self.model
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.storage.save()
            output = mock_stdout.getvalue().strip()
            self.assertTrue(output.startswith('{'))
            self.assertTrue(output.endswith('}'))
            self.assertIn(key, output)

    def test_set_attr(self):
        """Test set_attr method."""
        attr_name = "test_attribute"
        attr_value = "test_value"
        key = f"{type(self.model).__name__}.{self.model.id}"
        self.storage._objects[key] = self.model
        self.storage.set_attr(self.model, attr_name, attr_value)
        self.assertEqual(getattr(self.model, attr_name), attr_value)

    def test_reload(self):
        """Test reload method."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.storage.reload()
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, '')

    def test_serializer(self):
        """Test serializer method."""
        dt = datetime(2022, 1, 1, 12, 0, 0)
        self.assertEqual(self.storage.serializer(dt), dt.isoformat())

if __name__ == "__main__":
    unittest.main()
