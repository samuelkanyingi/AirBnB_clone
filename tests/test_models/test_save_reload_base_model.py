#!/usr/bin/python3
"""method to test class FileStorage"""
import unittest
import os
import json
import tempfile
from models import storage
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """Test class for FileStorage"""
    def setUp(self):
        """Set up a FileStorage instance for testing."""
        self.temp_file = tempfile.NamedTemporaryFile(delete=False)
        self.file_path = self.temp_file.name
        self.storage = FileStorage(self.file_path)
        self.my_model = BaseModel()

    def tearDown(self):
        """Clean up"""
        self.temp_file.close()
        os.remove(self.file_path)

    def test_init(self):
        """Test the initialization of FileStorage."""
        self.assertEqual(self.storage._FileStorage__file_path, self.file_path)
        self.assertIsInstance(self.storage._FileStorage__objects, dict)

    def test_all(self):
        """Test the all method."""
        objects = self.storage.all()
        self.assertIsInstance(objects, dict)
        self.assertEqual(objects, self.storage._FileStorage__objects)

    def test_new(self):
        """Test the new method."""
        self.storage.new(self.my_model)
        key = f"{self.my_model.__class__.__name__}.{self.my_model.id}"
        self.assertIn(key, self.storage._FileStorage__objects)

    def test_save(self):
        """Test the save method."""
        self.storage.new(self.my_model)
        self.storage.save()
        with open(self.file_path, 'r') as file:
            saved_data = json.load(file)

        key = f"{self.my_model.__class__.__name__}.{self.my_model.id}"
        self.assertIn(key, saved_data)

    def test_reload(self):
        """Test the reload method."""
        self.storage.new(self.my_model)
        self.storage.save()
        new_storage = FileStorage(self.file_path)
        new_storage.reload()
        key = f"{self.my_model.__class__.__name__}.{self.my_model.id}"
        self.assertIn(key, new_storage._FileStorage__objects)


if __name__ == '__main__':
    unittest.main()
