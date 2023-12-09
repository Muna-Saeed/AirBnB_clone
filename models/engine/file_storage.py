#!/usr/bin/env python3
""" file_storage.py """
from json.decoder import JSONDecodeError
from datetime import datetime
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """ File storage class """

    __file_path = "file.json"
    __objects = {}

    def destroy_object(self, obj):
        """ destory objects """

        key = f"{type(obj).__name__}.{obj.id}"
        self.__objects.pop(key, None)
        self.save()

    def all(self):
        """ returns all objecst """
        return self.__objects

    def new(self, ob):
        """ adds new object """
        key = f"{type(ob).__name__}.{ob.id}"
        FileStorage.__objects[key] = ob

    def save(self):
        """ saves to file """

        formated = {
            key: val.to_dict()
            for key, val in self.__objects.items()
        }
        with open(FileStorage.__file_path, "w") as f:
            json.dump(formated, f, default=self.serializer)

    def set_attr(self, obj, attr, value):
        """ sets   attr """

        setattr(obj, attr, value)
        key = f"{type(obj).__name__}.{obj.id}"
        FileStorage.__objects[key] = obj
        FileStorage.__objects[key].updated_at = datetime.now()
        self.save()

    @classmethod
    def reload(cls):
        """ reloads from file """

        try:
            with open(cls.__file_path, "r") as f:
                deserialized = json.load(f)
                if deserialized is None:
                    return
                for key, val in deserialized.items():
                    class_name = val['__class__']
                    class_type = globals()[class_name]

                    if hasattr(class_type, 'count_ob'):
                        class_type.count_ob += 1
                    cls.__objects[key] = class_type(**val)
        except (FileNotFoundError, JSONDecodeError):
            pass

    def serializer(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
