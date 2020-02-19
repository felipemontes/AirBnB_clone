#!/usr/bin/python3
'''Unittest BaseModel Modules'''

import unittest
import os
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    '''Unittest for BaseModel'''

    my_model = BaseModel()

    def testPass(self):
        '''Tests for attributes'''
        self.my_model.name = 'Holberton'
        self.my_model.my_number = 89
        self.my_model.save()

    def testValues(self):
        '''Tests for values in json'''
        my_model_json = self.my_model.to_dict()
        self.assertTrue(isinstance(self.my_model, BaseModel))
        self.assertEqual('BaseModel', my_model_json['__class__'])
        self.assertEqual(self.my_model.id, my_model_json['id'])
        self.assertEqual(self.my_model.name, my_model_json['name'])
        self.assertEqual(self.my_model.my_number, my_model_json['my_number'])

    def testInstances(self):
        '''comment'''
        self.assertIsInstance(self.my_model.id, str)
        self.assertIsInstance(self.my_model.created_at, datetime)
        self.assertIsInstance(self.my_model.updated_at, datetime)

if __name__ == '__main__':
    '''Main initializer'''
    unittest.main()
