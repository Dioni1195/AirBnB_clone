#!/usr/bin/python3
""" This module contains the storage class"""
import json
import os.path

import models

from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """ This class stores the represntation of the class in a file
        Args:
        __file_path(str): Path to the json file
        __objects(dict): Store all objects <class name>.id
    """
    __file_path = "file.json"
    __objects = dict()

    def all(self):
        """ This method returns __objects """
        return FileStorage.__objects

    def new(self, obj):
        """ Sets in __objects the obj
            Args:
            obj: The object to be stored"""
        obj_key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[obj_key] = obj

    def save(self):
        """ This method serialize __objects attr to JSON file """
        ser_dict = {}
        for key, value in FileStorage.__objects.items():
            ser_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as ser_file:
            json.dump(ser_dict, ser_file)

    def reload(self):
        """ Deserializes the JSON file to __objects """
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, encoding='utf-8') as des_file:
                loaded_dict = json.load(des_file)
                for key, value in loaded_dict.items():
                    identifier = value['__class__']
                    obj = globals()[identifier](**value)
                    FileStorage.__objects[key] = obj
        else:
            pass
