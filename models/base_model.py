#!/usr/bin/python3
"""
base_model.py

This module defines the BaseModel class, a fundamental class
 for object-relational mapping (ORM).
"""

import uuid
from datetime import datetime
import models


class BaseModel:
    """
    BaseModel class represents the base model for the ORM system.

    Attributes:
        - id (str): A unique identifier for each instance.
        - created_at (datetime): The date and time when
        - updated_at (datetime): The date and time when


    Methods:
        - __init__: Initializes a new instance of the BaseModel.
        - set_attr: Sets attributes or reloads data from a dictionary.
        - save: Saves changes to the storage system.
        - __str__: Returns a string representation of the object.
        - to_dict: Converts the object to a dictionary.
        - count: Counts the objects of the same class.
        - all: Prints all objects of the same class.
        - show: Shows the object with the provided ID.
        - update: Updates the object with the provided ID.
        - get_object: Gets an object with the provided ID.
        - destroy: Deletes an object from the dictionary of objects and saves.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize the BaseModel.
        If keyword arguments are provided, set attributes from the dictionary.
        Otherwise, generate a new ID and set creation and update timestamps.
        """
        if kwargs:
            self.set_attr(**kwargs)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def set_attr(self, **kwargs):
        """Set attributes or reload data from a dictionary."""
        for key, value in kwargs.items():
            if key != '__class__':
                if key == "created_at" or key == "updated_at":
                    value = datetime.fromisoformat(value)
                setattr(self, key, value)

    def save(self):
        """Save changes to the storage system."""
        self.updated_at = datetime.now()
        models.storage.save()

    def __str__(self):
        """Return a string representation of the object."""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def to_dict(self):
        """Convert the object to a dictionary."""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        exclude_attributes = ['models', 'storage']
        for attr in exclude_attributes:
            obj_dict.pop(attr, None)
            for key, value in obj_dict.items():
                if isinstance(value, datetime):
                    obj_dict[key] = value.isoformat()
        return obj_dict

    @classmethod
    def count(cls):
        """Count the objects of the same class."""
        c = 0
        clname = cls.__name__
        all_objects = models.storage.all()
        for key in all_objects.keys():
            if key.split(".")[0] == clname:
                c += 1
        print(c)

    @classmethod
    def all(cls, id=0):
        """Print all objects of the same class."""
        all_objects = models.storage.all()
        clsname = cls.__name__
        arr = []
        for key in all_objects.keys():
            sp = key.split(".")
            obj = all_objects[key]
            if (sp[0] == clsname) and obj.__class__.__name__ == clsname:
                arr.append(str(obj))
        print(arr)

    @classmethod
    def show(cls, id):
        """Show the object with the provided ID."""
        obj = cls.get_object(id)
        if obj:
            print(str(obj))
            return
        print("** no instance found **")

    @classmethod
    def update(cls, id, attr, value):
        """Update the object with the provided ID."""
        obj = cls.get_object(id)
        if obj:
            models.storage.set_attr(obj, attr, value)
            return
        print("** no instance found **")

    @classmethod
    def get_object(cls, id):
        """Get an object with the provided ID."""
        all_objects = models.storage.all()
        clsname = cls.__name__
        for key in all_objects.keys():
            sp = key.split(".")
            obj = all_objects[key]
            obname = obj.__class__.__name__
            if (sp[0] == clsname) and obname == clsname and obj.id == id:
                return obj
        return False

    @classmethod
    def destroy(cls, id):
        """Delete an object from the dictionary of objects and save."""
        obj = cls.get_object(id)
        if obj:
            models.storage.destroy_object(obj)
            return
        print("** no instance found **")
