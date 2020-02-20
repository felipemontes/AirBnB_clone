#!/usr/bin/python3
'''Unittest BaseModel Modules'''

import unittest
import os
import pep8
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    '''Unittest for BaseModel'''

    my_model = BaseModel()

    def setUp(self):
        '''Sets up methods'''
        try:
            os.remove("file.json")
        except:
            pass
        FileStorage._FileStorage__objects = {}

    def tearDown(self):
        '''Resets file.json'''
        try:
            os.remove("file.json")
        except:
            pass

    def testArgs(self):
        '''No arguments'''
        with self.assertRaises(TypeError) as e:
            BaseModel.__init__()
        msg = "__init__() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), msg)

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

    def test_exist(self):
        '''Tests if the class exists'''
        self.assertEqual(str(type(self.my_model)),
                         "<class 'models.base_model.BaseModel'>")

    def testInstances(self):
        '''Tests for if it's an instance'''
        self.assertIsInstance(self.my_model.id, str)
        self.assertIsInstance(self.my_model.created_at, datetime)
        self.assertIsInstance(self.my_model.updated_at, datetime)

    def testSave(self):
        ''' Test for save method '''
        self.my_model.first_name = 'brayan'
        self.my_model.save()
        dic = self.my_model.to_dict()
        self.assertEqual(dic['first_name'], 'brayan')

    def test_save_1(self):
        ''' Test save method '''
        self.my_model.first_name = 'brayan'
        self.my_model.save()

        self.assertIsInstance(self.my_model.id, str)
        self.assertIsInstance(self.my_model.created_at, datetime)
        self.assertIsInstance(self.my_model.updated_at, datetime)

        dic1 = self.my_model.to_dict()

        self.my_model.first_name = 'felipe'
        self.my_model.save()

        dic2 = self.my_model.to_dict()

        self.assertEqual(dic1['created_at'], dic2['created_at'])
        self.assertNotEqual(dic1['updated_at'], dic2['updated_at'])

    def test_pep8_conformance(self):
        '''Test that we conform to PEP8.'''
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

if __name__ == '__main__':
    '''Main initializer'''
    unittest.main()
