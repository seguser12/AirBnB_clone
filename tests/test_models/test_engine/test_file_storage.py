#!/usr/bin/python3
'''test for file_storage'''

import unittest
from models import storage
from models.base_model import BaseModel
import os


class TestFileStorage(unittest.TestCase):
    '''Test class for FileStorage'''

    @classmethod
    def setUpClass(cls):
        '''set up for test'''
        cls.my_model = BaseModel()
        cls.my_model.name = 'Jaoh'
        cls.my_model.number = '8'
        cls.obj = storage.all()

    @classmethod
    def teardown(cls):
        '''tears down all instance at end of test'''
        del cls.my_model
        del cls.obj

        try:
            os.remove('file.json')
        except Exception:
            pass

    def test_new(self):
        '''test new method'''
        storage.new(self.my_model)
        key = "{}.{}".format(self.my_model.__class__.__name__,
                             self.my_model.id)
        self.assertIsNotNone(self.obj[key])

    def test_all(self):
        '''test all method of class'''
        self.assertIsNotNone(self.obj)
        self.assertIsInstance(self.obj, dict)

    def test_save(self):
        storage.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_reload(self):
        '''test save method'''
        storage.save()
        storage.reload()
        for values in self.obj.values():
            load = values
        self.assertEqual(self.my_model.to_dict()['id'], load.to_dict()['id'])

    def test_type_path(self):
        '''test _file_path is str'''
        self.assertEqual(type(storage._FileStorage__file_path), str)
