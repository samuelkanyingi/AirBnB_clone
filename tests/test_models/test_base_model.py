#!/usr/bin/python3
"""module to test class  TestBaseModel"""
import unittest
from models.base_model import BaseModel
from datetime import datetime, timedelta
import uuid


class TestBaseModel(unittest.TestCase):
    """child class to test methods"""
    def test_str(self):
        """test string representation"""
        my_model = BaseModel()
        self.assertAlmostEqual(my_model.created_at,
                               datetime.now(), delta=timedelta(seconds=1))

    def test_save(self):
        my_model = BaseModel()
        initial_update = my_model.updated_at
        my_model.save()
        self.assertNotEqual(my_model.updated_at, initial_update)
        self.assertAlmostEqual(my_model.updated_at, datetime.now(),
                               delta=timedelta(seconds=1))

    def test_to_dict(self):
        my_model = BaseModel()
        my_model.name = "My first Model"
        my_model.my_number = 89

        my_model.save()
        my_model_dict = my_model.to_dict()
        self.assertIn('__class__', my_model_dict)
        self.assertIn('created_at', my_model_dict)
        self.assertIn('updated_at', my_model_dict)
        self.assertIn('id', my_model_dict)
        self.assertIn('name', my_model_dict)
        self.assertIn('my_number', my_model_dict)
        self.assertEqual(my_model_dict['__class__'], 'BaseModel')
        self.assertEqual(my_model_dict['created_at'],
                         my_model.created_at.isoformat())
        self.assertEqual(my_model_dict['updated_at'],
                         my_model.updated_at.isoformat())
        self.assertEqual(my_model_dict['id'], my_model.id)
        self.assertEqual(my_model_dict['name'], my_model.name)
        self.assertEqual(my_model_dict['my_number'], my_model.my_number)


if __name__ == '__main__':
    unittest.main()
