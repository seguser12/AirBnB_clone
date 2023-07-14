#!/usr/bin/python3
'''Models Module for project'''

from uuid import uuid4
from datetime import datetime
from models import storage


class BaseModel:
    '''BaseModel class for the AirBnB project'''

    def __init__(self, *args, **kwargs):
        '''public instance attributes initialization'''
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.fromisoformat(value)
                if key != '__class__':
                    setattr(self, key, value)
            if 'id' not in kwargs.keys():
                setattr(self, 'id', str(uuid4()))
            if 'created_at' not in kwargs.keys():
                setattr(self, 'created_at', datetime.now())
            if 'updated_at' not in kwargs.keys():
                setattr(self, 'updated_at', datetime.now())

        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        '''string representation of class'''
        cls_name = type(self).__name__
        dict_rep = self.__dict__
        str_rep = "[{}] ({}) {}".format(cls_name, self.id, dict_rep)
        return (str_rep)

    def save(self):
        '''updates the public instance attribute updated_at'''
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        '''Returns a dictionary containing all keys/values of __dict__'''
        to_dict = self.__dict__.copy()
        to_dict['__class__'] = type(self).__name__
        to_dict['created_at'] = to_dict['created_at'].isoformat()
        to_dict['updated_at'] = to_dict['updated_at'].isoformat()
        return to_dict
