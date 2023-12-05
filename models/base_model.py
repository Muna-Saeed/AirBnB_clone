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
                setattr(self, key, value)
            
    def save(self):
        self.updated_at = datetime.now()
        models.storage.save()

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"



    def to_dict(self):
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__

        # Exclude attributes that may cause circular references
        exclude_attributes = ['models', 'storage']
        for attr in exclude_attributes:
            obj_dict.pop(attr, None)
            for key, value in obj_dict.items():
                if isinstance(value, datetime):
                    obj_dict[key] = value.isoformat()
        return obj_dict
