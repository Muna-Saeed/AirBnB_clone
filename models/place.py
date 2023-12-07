#!/usr/bin/env python3
""" place.py """
from models.base_model import BaseModel
import models


class Place(BaseModel):
    """ Place class """
    city_id = ""          # string: empty string (will be the City.id)
    user_id = ""          # string: empty string (will be the User.id)
    name = ""             # string: empty string
    description = ""      # string: empty string
    number_rooms = 0      # integer: 0
    number_bathrooms = 0  # integer: 0
    max_guest = 0         # integer: 0
    price_by_night = 0    # integer: 0
    latitude = 0.0        # float: 0.0
    longitude = 0.0       # float: 0.0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        """ initialize super """
        super().__init__(*args, **kwargs)
