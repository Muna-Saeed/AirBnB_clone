#!/usr/bin/env python3
""" models/city.py """
from models.base_model import BaseModel


class City(BaseModel):
    """ Class city """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initialize User instance"""
        super().__init__(*args, **kwargs)
