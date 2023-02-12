#!/usr/bin/python3
'''test city module'''

from tests.test_models.test_base_model import TestBaseModel
from models.city import City


class test_City(TestBaseModel):
    """ test city class"""

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """ test state id"""
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """ test name """
        new = self.value()
        self.assertEqual(type(new.name), str)
