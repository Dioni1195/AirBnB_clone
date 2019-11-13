#!/usr/bin/python3
""" This module contains the base class, it is important to
save all the common attrs and methods of the other classes"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """This class maintain the common attrs and methods between other classes.
    Register data and simple audit information
    Attrs:
        - id(str): The unique identificator of the instance
        - created_at(date): It stores the date when the instance was created
        - updated_at(date): It sotres the date when the instance was updated
    """
    def __init__(self, *args, **kwargs):
        """Instantiates the attributes of the BaseModel class"""
        if args is not None and len(args) > 0:
            pass
        if kwargs:
            for key, item in kwargs.items():
                if key in ['created_at', 'updated_at']:
                    item = datetime.strptime(item, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, item)
                elif key == "__class__":
                    continue
                else:
                    setattr(self, key, item)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """This method sets the way that the instance is printed """
        name_cls = self.__class__.__name__
        return "[{}] ({}) {}".format(name_cls, self.id, self.__dict__)

    def save(self):
        """ This method saves the changes made in the instance """
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """ This method returns a dict representation of the instance """
        new_dict = {}
        for key, item in self.__dict__.items():
            if key in ['created_at', 'updated_at']:
                new_dict[key] = item.isoformat()
            else:
                new_dict[key] = item
        new_dict['__class__'] = self.__class__.__name__
        return new_dict
