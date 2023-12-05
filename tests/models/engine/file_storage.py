#!/usr/bin/env python3
""" file_storage.py """
from json.decoder import JSONDecodeError
from datetime import datetime
import json
from models.base_model import BaseModel


class FileStorage:
    __file_path = "file.json"
    __objects = {}
    
    def destroy_object(self, obj):
        key = f"{type(obj).__name__}.{obj.id}"
        self.__objects.pop(key, None)
        self.save()


    def all(self):
        return self.__objects

    def new(self, obj):
        key = f"{type(obj).__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        serialized = {
            key: val.to_dict()
            for key, val in self.__objects.items()
        }
        with open(FileStorage.__file_path, "w") as f:
            json.dump(serialized, f, default=lambda o: o.isoformat() if isinstance(o, datetime) else o)

    def reload(self):
        try:
            with open(FileStorage.__file_path, "r") as f:
                deserialized = json.load(f)
            FileStorage.__objects = {
                key: BaseModel(**val)
                for key, val in deserialized.items()
            }
        except (FileNotFoundError, JSONDecodeError):
            # No need for error handling here
            pass
