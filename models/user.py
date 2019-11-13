#!/usr/bin/python3
""" This module contains the class User """
from .base_model import BaseModel


class User(BaseModel):
    """ This class allows to create Users
        attrs:
        email(str): The email of the user
        password(str): The password of the user in platform
        first_name(str): The first name of the user
        last_name(str): The last name of the user
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
