#!/usr/bin/python3
""" This module contains the class State """
from .base_model import BaseModel


class State(BaseModel):
    """ This class allows to create States
        attrs:
        name(str): The name of the State
    """
    name = ""
