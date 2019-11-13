#!/usr/bin/python3
""" This module contains the class Place """
from .base_model import BaseModel


class Place(BaseModel):
    """ This class allows to create Place
        attrs:
        name(str): The name of the Place
        city_id(str): The id of the city
        user_id(str): The id of the user
        description(str): The description of the place
        number_rooms(int): The number of rooms of the place
        number_bathrooms(int): The number of bathrooms of the place
        max_guest(int): The maximun of permitted guest in the place
        price_by_night(int): The price per night of the place
        latitude(float): The latitude of the place
        longitude(float): The longitude of the place
        amenity_ids(list of str): The list of amenity
    """
    name = ""
    city_id = ""
    user_id = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
