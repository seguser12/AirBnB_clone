#!/usr/bin/python3
""" test state module """

from tests.test_models.test_base_model import TestBaseModel
from models.state import State


class test_state(TestBaseModel):
    """ test state class """

    def __init__(self, *args, **kwargs):
        """ test class initialization """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name(self):
        """ test name"""
        new = self.value()
        self.assertEqual(type(new.name), str)
