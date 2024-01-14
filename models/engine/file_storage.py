#!/usr/bin/python3
import json
from models.base_model import BaseModel


class FileStorage:
    """A class for handling storage to/from a JSON file."""
    def __init__(self, file_path):
        """class constructor"""
        self.__file_path = file_path
        self.__objects = {}

    def all(self):
        """Retrieve all objects in the storage"""
        return self.__objects

    def new(self, obj):
        """Add a new object to the storage"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Save objects to the JSON file"""
        serialized_objects = {}
        for key, value in self.__objects.items():
            serialized_objects[key] = value.to_dict()
            with open(self.__file_path, 'w') as file:
                json.dump(serialized_objects, file)

    def reload(self):
        """Reload objects from the JSON file"""
        try:
            with open(self.__file_path, 'r') as file:
                data = json.load(file)
                for key, value in data.items():
                    class_name, obj_id = key.split('.')
                    class_instance = globals().get(class_name)
                    if class_instance:
                        instance = class_instance(**value)
                        self.__objects[key] = instance
        except FileNotFoundError:
            pass
