#!/usr/bin/python3
""" user test module """

from tests.test_models.test_base_model import TestBaseModel
from models.user import User


class test_User(TestBaseModel):
    """ test user class """

    def __init__(self, *args, **kwargs):
        """ test initialization """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """ test first name """
        new = self.value()
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """ test last_name attribute """
        new = self.value()
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """ test email """
        new = self.value()
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """test password """
        new = self.value()
        self.assertEqual(type(new.password), str)
