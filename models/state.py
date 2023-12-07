#!/usr/bin/env python3
""" models/state.py """
from models.base_model import BaseModel
import models


class State(BaseModel):
    """class State"""
    name = ""


    def __init__(self, *args, **kwargs):
        """Initialize User instance"""
        super().__init__(*args, **kwargs)

