#!/usr/bin/python3
""" This module contains the class Amenity """
from .base_model import BaseModel


class Amenity(BaseModel):
    """ This class allows to create Amenity
        attrs:
        name(str): The name of the Amenity
    """
    name = ""
