#!/usr/bin/python3
""" This module contains the class Review """
from .base_model import BaseModel


class Review(BaseModel):
    """ This class allows to create Reviews
        attrs:
        text(str): The text of the review
        place_id(str): The place id
        user_id(str) = The user id
    """
    text = ""
    place_id = ""
    user_id = ""
