#!/usr/bin/python3
"""File Storage Unit Tests"""

import models
import os
import sys
import pep8
import unittest
from models import storage
from models.user import User
from models import FileStorage
from models.city import City
from datetime import datetime
from models.place import Place
from models.review import Review
from models.state import State
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.amenity import Amenity


class Test_FileStorage(unittest.TestCase):
    """
    Test cases for class FileStorage
    """

    def test_docstring(self):
        """Checks if docstring exist"""
        self.assertTrue(len(FileStorage.__doc__) > 1)
        self.assertTrue(len(FileStorage.all.__doc__) > 1)
        self.assertTrue(len(FileStorage.new.__doc__) > 1)
        self.assertTrue(len(FileStorage.save.__doc__) > 1)
        self.assertTrue(len(FileStorage.reload.__doc__) > 1)

    def test_pep8(self):
        """Pep8 Test"""
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(result.total_errors, 0, "fix pep8")

    def test_instantiation(self):
        """Tests for proper instantiation"""
        temp_storage = FileStorage()
        self.assertIsInstance(temp_storage, FileStorage)

    def test_saves_new_instance(self):
        """Tests if file is being created """

        def touch(file_path):
            with open(file_path, 'a'):
                os.utime(file_path, None)

        obj = BaseModel()
        models.storage.new(obj)
        models.storage.save()
        touch(file_path="file.json")
        file_exist = os.path.exists(self.file_path)
        self.assertTrue(file_exist)

    def test_all(self):
        """Tests the all method"""
        temp_storage = FileStorage()
        temp_dict = temp_storage.all()
        self.assertIsNotNone(temp_dict)
        self.assertEqual(type(temp_dict), dict)

    def test_new(self):
        """Tests the new method"""
        temp_storage = FileStorage()
        temp_dict = temp_storage.all()
        Dionisio = User()
        Dionisio.id = 1991
        Dionisio.name = "SDVSF"
        temp_storage.new(Dionisio)
        class_name = Dionisio.__class__.__name__
        key = "{}.{}".format(class_name, str(Holberton.id))
        self.assertIsNotNone(temp_dict[key])

    def test_attributes(self):
        """Test the attributes for FileStorage class"""
        self.assertTrue(isinstance(storage._FileStorage__objects, dict))
        self.assertTrue(isinstance(storage._FileStorage__file_path, dict))

    def test_reload(self):
        """Tests the reaload method """
        Dionisio = FileStorage()
        sizeofobj = len(Dionisio._FileStorage__objects)
        self.assertGreater(sizeofobj, 0)
