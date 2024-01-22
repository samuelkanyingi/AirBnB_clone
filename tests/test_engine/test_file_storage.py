#!/usr/bin/python3
import unittest
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):

    def setUp(self):
        """Set up the FileStorage instance for testing."""
        self.file_path = "test_file.json"
        self.storage = FileStorage()
        self.storage._FileStorage__file_path = self.file_path

    def tearDown(self):
        """Clean up the test environment."""
        try:
            os.remove(self.file_path)
        except FileNotFoundError:
            pass

    def test_all(self):
        """Test the all method of FileStorage."""
        self.assertIsInstance(self.storage.all(), dict)

    def test_new(self):
        """Test the new method of FileStorage."""
        user = User()
        self.storage.new(user)
        self.assertIn("User." + user.id, self.storage.all())

    def test_save_reload(self):
        """Test the save and reload methods of FileStorage."""
        user = User()
        self.storage.new(user)
        self.storage.save()
        new_storage = FileStorage()
        new_storage.reload()
        self.assertIn("User." + user.id, new_storage.all())

if __name__ == '__main__':
    unittest.main()

