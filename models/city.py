#!/usr/bin/python3
""" This module contains the class City """
from .base_model import BaseModel


class City(BaseModel):
    """ This class allows to create Cities
        attrs:
        name(str): The name of the City
        state_id(str): The state id
    """
    name = ""
    state_id = ""
