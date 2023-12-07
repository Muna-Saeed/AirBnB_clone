#!/usr/bin/env python3
""" amenity.py """
from models.base_model import BaseModel
import models

class Amenity(BaseModel):
    """ Amenity class """
    name = ""  # string: empty string


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
