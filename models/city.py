#!/usr/bin/python3
'''model city module'''

from .base_model import BaseModel


class City(BaseModel):
    '''city class iunherit from Basemodel class'''
    state_id = ''
    name = ''
