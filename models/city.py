#!/usr/bin/python3
'''city module'''

from models.base_model import BaseModel


class City(BaseModel):
    '''city class inheriting from baseModel class'''
    state_id = ''
    name = ''
