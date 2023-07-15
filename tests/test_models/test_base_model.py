#!/usr/bin/python3
'''test basemodel module'''

import unittest
from models.base_model import BaseModel
from datetime import datetime
import pep8


class TestBaseModel(unittest.TestCase):
    '''Test for BaseModel class'''
    def setUp(self):
        '''prepares setup for tests'''
        self.model = BaseModel()
        self.model.name = "My First Model"
        self.model.my_number = 89

    def tearDown(self):
        '''disposes created instances for tests'''
        self.model = None

    def test_pep8_baseModel(self):
        '''Testing for pep8 compliance'''
        style = pep8.StyleGuide(quiet=True)
        code_style = style.check_files(['models/base_model.py'])
        self.assertEqual(code_style.total_errors, 0, 'fix pep8')

    def text_check_baseModel_docstring(self):
        '''checking if docstrings exists'''
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertisNotNOne(BaseModel.__init__.__doc__)
        self.assertisNotNOne(BaseModel.__str__.__doc__)
        self.assertisNotNOne(BaseModel.save.__doc__)
        self.assertisNotNOne(BaseModel.to_dict.__doc__)

    def testInstanceAttributes(self):
        '''test basemodel instance attributes created'''
        self.assertIsInstance(self.model.id, str)
        self.assertIsInstance(self.model.name, str)
        self.assertIsInstance(self.model.my_number, int)
        self.assertIsInstance(self.model.created_at, datetime)
        self.assertIsInstance(self.model.updated_at, datetime)

    def testInstanceAttributesValues(self):
        '''test basemodel instance attribute values'''
        self.assertEqual(self.model.name, "My First Model")
        self.assertEqual(self.model.my_number, 89)

    def testInstanceAttributesMethods(self):
        '''test basemodel methods'''
        self.assertTrue(hasattr(self.model, '__init__'))
        self.assertTrue(hasattr(self.model, 'save'))
        self.assertTrue(hasattr(self.model, 'to_dict'))

    def test_init_method(self):
        '''Test baseModel init method'''
        self.assertIsInstance(self.model, BaseModel)

    def test_save_method(self):
        '''Test the baseModel save method'''
        self.model.save()
        self.assertNotEqual(self.model.created_at,
                            self.model.updated_at)

    def test_to_dict_method(self):
        '''Test the to_dict method of BaseModel'''
        model_json = self.model.to_dict()
        self.assertEqual(model_json.__class__, dict)
        self.assertEqual(model_json['__class__'], 'BaseModel')
        self.assertIsInstance(model_json['__class__'], str)
        self.assertIsInstance(model_json['created_at'], str)
        self.assertIsInstance(model_json['updated_at'], str)
