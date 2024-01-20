#!/usr/bin/python3
""" Write a class Amenity that inherits from BaseModel """
from models.base_model import BaseModel


class Amenity(BaseModel):
    """ A class that inherits from BaseModel """
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(kwargs)
