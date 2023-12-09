#!/usr/bin/python3
""" base_model.py """
import uuid
from datetime import datetime
import models


class BaseModel:
    """ BaseModel class
     """

    def __init__(self, *args, **kwargs):
        """ initialize """
        if kwargs:
            self.set_attr(**kwargs)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def set_attr(self, **kwargs):
        """ sets attributes or reloaded data """
        for key, value in kwargs.items():
            if key != '__class__':
                if key == "created_at" or key == "updated_at":
                    value = datetime.fromisoformat(value)
                setattr(self, key, value)

    def save(self):
        """ saves the chanage to file """
        self.updated_at = datetime.now()
        models.storage.save()

    def __str__(self):
        """ return str reprasentation of object """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def to_dict(self):
        """ object to dictionary """
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
        """ counts the objects of the same class """
        c = 0
        clname = cls.__name__
        all = models.storage.all()
        for key in all.keys():
            if key.split(".")[0] == clname:
                c += 1
        print(c)

    @classmethod
    def all(cls, id=0):
        """ prints all objects that are same class """
        all = models.storage.all()
        clsname = cls.__name__
        arr = []
        for key in all.keys():
            sp = key.split(".")
            obj = all[key]
            if (sp[0] == clsname) and obj.__class__.__name__ == clsname:
                arr.append(str(obj))
        print(arr)

    @classmethod
    def show(cls, id):
        """ shows the object that hass the provied id """

        obj = cls.get_object(id)
        if obj:
            print(str(obj))
            return
        print("** no instance found **")

    @classmethod
    def update(cls, id, attr, value):
        """ updates the object """
        obj = cls.get_object(id)
        if obj:
            models.storage.set_attr(obj, attr, value)
            return
        print("** no instance found **")

    @classmethod
    def get_object(cls, id):
        """ gets an object and returns it """
        all = models.storage.all()
        clsname = cls.__name__
        for key in all.keys():
            sp = key.split(".")
            obj = all[key]
            obname = obj.__class__.__name__
            if (sp[0] == clsname) and obname == clsname and obj.id == id:
                return obj
        return False

    @classmethod
    def destroy(cls, id):
        """ delates and object from the dict objecst and saves """
        obj = cls.get_object(id)
        if obj:
            models.storage.destroy_object(obj)
            return
        print("** no instance found **")
