#!/usr/bin/python3
'''Models Module for project'''

from uuid import uuid4
from datetime import datetime


class BaseModel:
    '''BaseModel class for the AirBnB project'''

    def __init__(self):
        '''public instance attributes initialization'''
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        '''string representation of class'''
        cls_name = type(self).__name__
        dict_rep = self.__dict__
        str_rep = "[{}] ({}) {}".format(cls_name, self.id, dict_rep) 
        return (str_rep)

    def save(self):
        '''updates the public instance attribute updated_at'''
        self.updated_at = datetime.now()

    def to_dict(self):
        '''Returns a dictionary containing all keys/values of __dict__'''
        dict = self.__dict__.copy()
        dict['__class__'] = type(self).__name__
        dict['created_at'] = dict['created_at'].isoformat()
        dict['updated_at'] = dict['updated_at'].isoformat()
        return dict
