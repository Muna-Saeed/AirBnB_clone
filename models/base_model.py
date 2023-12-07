#!/usr/bin/env python3
import uuid
from datetime import datetime
import models



class BaseModel:
    """ base class """
    def __init__(self, *args, **kwargs):
        if kwargs:
            self.set_attr(**kwargs)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)


    def set_attr(self, **kwargs):
        for key, value in kwargs.items():
            if key != '__class__':
                if key == "created_at" or key == "updated_at":
                    value = datetime.fromisoformat(value)
                setattr(self, key, value)

    def save(self):
        self.updated_at = datetime.now()
        models.storage.save()

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def to_dict(self):
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
        c = 0
        clname = cls.__name__
        all = models.storage.all()
        for key in all.keys():
            if key.split(".")[0] == clname:
                c += 1
        print(c)

    @classmethod
    def all(cls, id=0):
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
        obj = cls.get_object(id)
        if obj:
            print(str(obj))
            return
        print("** no instance found **")


    @classmethod
    def update(cls, id, attr, value):
        obj = cls.get_object(id);
        if obj:
            models.storage.set_attr(obj, attr, value)
            return
        print("** no instance found **")

    @classmethod
    def get_object(cls, id):
        all = models.storage.all()
        clsname = cls.__name__
        for key in all.keys():
            sp = key.split(".")
            obj = all[key]
            if (sp[0] == clsname) and obj.__class__.__name__ == clsname and obj.id == id:
                return obj
        return False

    @classmethod
    def destroy(cls, id):
        obj = cls.get_object(id);
        if obj:
            models.storage.destroy_object(obj)
            return
        print("** no instance found **")
