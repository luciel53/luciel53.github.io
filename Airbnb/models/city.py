#!/usr/bin/python3
""" Write a class City that inherits from BaseModel """
from models.base_model import BaseModel


class City(BaseModel):
    """ A class that inherits from BaseModel """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(kwargs)
