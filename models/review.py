#!/usr/bin/python3
'''model review module'''

from .base_model import BaseModel


class Review(BaseModel):
    '''review class inherits from basemodel'''
    place_id = ''
    user_id = ''
    text = ''
