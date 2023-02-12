#!/usr/bin/python3
'''model user module'''

from .base_model import BaseModel


class User(BaseModel):
    '''user class inheriting from BaseModel Class'''
    email = ""
    password = ""
    first_name = ""
    last_name = ""
