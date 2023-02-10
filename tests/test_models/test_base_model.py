#!/usr/bin/python3
'''test_base model module'''

import unittest
from models.base_model import BaseModel
import pep8
import os


class TestBaseModel(unittest.TestCase):
    '''Test class for BaseModel class'''
    @classmethod
    def setUpClass(cls):
        '''setup class method for test'''
        cls.my_model = BaseModel()
        cls.my_model.name = "My First Model"
        cls.my_model.my_number = 89

    @classmethod
    def teardown(cls):
        '''tear down test at the end'''
        del cls.my_model

    def test_pep8(self):
        '''test code follows pep8 styleguid'''
        style = pep8.StyleGuide()
        filenames = []
        for root, _, files in os.walk('models/'):
            python_files = [f for f in files if f.endswith('.py')]
            for file in python_files:
                filename = '{0}/{1}'.format(root, file)
                filenames.append(filename)
        check = style.check_files(filenames)
        self.assertEqual(check.total_errors, 0, 
                       'PEP8 errors: %d' % check.total_errors)

    def test_check_BaseModel_documentation(self):
        '''check to see class and methods are properly documented'''
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_BaseModel_methods_exist(self):
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))

    def test_instance_attribute(self):
        '''test if instance attribute is properly assigned'''
        self.assertIsInstance(self.my_model, type(BaseModel()))

    def test_BaseModel_save(self):
        '''test for BaseModel save method'''
        self.my_model.save()
        self.assertNotEqual(self.my_model.created_at, self.my_model.updated_at)

    def test_BaseModel_to_dict(self):
        '''test for BaseModel to_dict method'''
        my_model_json = self.my_model.to_dict()
        self.assertIsInstance(my_model_json['created_at'], str)
        self.assertIsInstance(my_model_json['updated_at'], str)
        self.assertIsInstance(my_model_json['my_number'], int)
        self.assertIsInstance(my_model_json['name'], str)
        self.assertIsInstance(my_model_json['id'], str)


if __name__ == '__main__':
    unittest.main()
