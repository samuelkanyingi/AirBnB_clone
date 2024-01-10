#!/usr/bin/python3
"""
The module is base_module
parent class is BaseModule
"""

import uuid
from datetime import datetime

class BaseModel:

    """BaseModel class that defines all instances
    and methods for other classes
    """
    def __init__(self, *args, **kwargs):
        """This is the class instantiator"""
        if kwargs:
            for key, value in kwargs.items():
                setattr(self,key, value)
        if 'id' not in kwargs:
            self.id = str(uuid.uuid4())

        if 'created_at' not in kwargs:
            self.created_at = datetime.now()

        if 'updated_at' not in kwargs:
            self.updated_at = datetime.now()

    def __str__(self):
        """Return a string representation of the object."""
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Update the updated_at attribute with the current datetime."""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Return a dictionary representation of the object."""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict


