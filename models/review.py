#!/usr/bin/env python3
""" review.py """
from models.base_model import BaseModel
import models


class Review(BaseModel):
    """ Review class """
    place_id = ""  # string: empty string (will be the Place.id)
    user_id = ""   # string: empty string (will be the User.id)
    text = ""      # string: empty string

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
