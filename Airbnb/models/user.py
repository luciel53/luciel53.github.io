#!/usr/bin/python3
""" Write a class User that inherits from BaseModel """
from models.base_model import BaseModel


class User(BaseModel):
    """ A class that inherits from BaseModel """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(kwargs)
