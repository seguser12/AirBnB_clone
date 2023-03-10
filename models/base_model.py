#!/usr/bin/python3
'''AirBnB BaseModel module'''

from uuid import uuid4
from datetime import datetime
from models import storage


class BaseModel:
    '''defines all common attributes/methods for other classes'''

    def __init__(self, *args, **kwargs):
        '''class constructor for BaseModel'''
        if not kwargs:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        if kwargs is not None:
            for key, value in kwargs.items():
                if key in ('created_at', 'updated_at'):
                    value = datetime.fromisoformat(value)
                if key != '__class__':
                    setattr(self, key, value)
            '''if 'id' not in kwargs.keys():
                self.id  = str(uuid4())
            if 'created_at' not in kwargs.keys():
                self.created_at = datetime.now()
            if 'updated_at' not in kwargs.keys():
                self.updated_at = datetime.now()'''

    def __str__(self):
        '''str magic method to print str rep'''
        str_rep = f"[{__class__.__name__}] ({self.id}) {self.__dict__}"
        return str_rep

    def save(self):
        '''updates the public instance attribute update_at'''
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        '''returns a dictionary containing all keys/values of __dict__'''
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = self.__class__.__name__
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        return my_dict
