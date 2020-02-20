#!/usr/bin/python3
""" Unittest FileStorage """
import unittest
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State
from models.engine.file_storage import FileStorage
from datetime import datetime
import json
import os
import pep8


class TestFileStorage(unittest.TestCase):
    """ Test cases for FileStorage"""

    obj = BaseModel()

    def setUp(self):
        """ Sets up all methods"""
        try:
            os.remove("file.json")
        except:
            pass
        FileStorage._FileStorage__objects = {}

    def tearDown(self):
        """ Removes the file """
        try:
            os.remove("file.json")
        except:
            pass

    def testIsInstance(self):
        """ Checks if it's an instance """
        self.assertIsInstance(storage, FileStorage)

    def test_exist(self):
        """ checks if the class exist """
        obj = BaseModel()
        self.assertEqual(str(type(obj)),
                         "<class 'models.base_model.BaseModel'>")

    def test_empty(self):
        """ Test empty file """
        self.assertEqual(storage.all(), {})

    def test_create_basemodel(self):
        """ Test create basemodel"""
        obj = BaseModel()
        key = obj.__class__.__name__ + '.' + obj.id
        dic = {key: obj}
        self.assertEqual(storage.all(), dic)

    def test_create_user(self):
        """ Test create User """
        obj = User()
        key = obj.__class__.__name__ + '.' + obj.id
        dic = {key: obj}
        self.assertEqual(storage.all(), dic)

    def test_create_city(self):
        """ Test create City """
        obj = City()
        key = obj.__class__.__name__ + '.' + obj.id
        dic = {key: obj}
        self.assertEqual(storage.all(), dic)

    def test_create_amenity(self):
        """ Test create Amenity """
        obj = Amenity()
        key = obj.__class__.__name__ + '.' + obj.id
        dic = {key: obj}
        self.assertEqual(storage.all(), dic)

    def test_create_place(self):
        """ Test create Place """
        obj = Place()
        key = obj.__class__.__name__ + '.' + obj.id
        dic = {key: obj}
        self.assertEqual(storage.all(), dic)

    def test_create_review(self):
        """ Test create Review """
        obj = Review()
        key = obj.__class__.__name__ + '.' + obj.id
        dic = {key: obj}
        self.assertEqual(storage.all(), dic)

    def test_create_state(self):
        """ Test create State """
        obj = State()
        key = obj.__class__.__name__ + '.' + obj.id
        dic = {key: obj}
        self.assertEqual(storage.all(), dic)

    def test_input_1(self):
        """ Test no arguments """
        with self.assertRaises(TypeError):
            storage.new()

    def test_input_2(self):
        """ test multiple arguments """
        obj = BaseModel()
        with self.assertRaises(TypeError):
            storage.new(obj, obj)

    def test_path(self):
        ''' test the file path '''
        self.assertEqual(hasattr(FileStorage, '_FileStorage__file_path'), True)
        self.assertEqual(hasattr(FileStorage, '_FileStorage__objects'), True)

    def test_save(self):
        ''' test save '''
        self.obj.save()
        self.assertEqual(os.path.exists(storage._FileStorage__file_path), True)
        self.assertEqual(storage.all(), storage._FileStorage__objects)

    def test_save_self(self):
        ''' test save self'''
        err = "save() takes 1 positional argument but 2 were given"
        with self.assertRaises(TypeError) as e:
            FileStorage.save(self, 100)

        self.assertEqual(str(e.exception), err)

    def test_save_key(self):
        ''' Test to check save method '''
        self.obj.full_name = "BaseModel Instance"
        self.obj.save()
        dic1 = self.obj.to_dict()
        all_objs = storage.all()

        key = dic1['__class__'] + "." + dic1['id']
        self.assertEqual(key in all_objs, True)

    def test_basemodel(self):
        ''' Test BaseModel'''
        self.obj.my_name = "Betty"
        self.obj.save()
        dic1 = self.obj.to_dict()
        all_objs = storage.all()

        key = dic1['__class__'] + "." + dic1['id']

        self.assertEqual(key in all_objs, True)
        self.assertEqual(dic1['my_name'], "Betty")

        create1 = dic1['created_at']
        update1 = dic1['updated_at']

        self.obj.my_name = "Holberton"
        self.obj.save()
        dic2 = self.obj.to_dict()
        all_objs = storage.all()

        self.assertEqual(key in all_objs, True)

        create2 = dic2['created_at']
        update2 = dic2['updated_at']

        self.assertEqual(create1, create2)
        self.assertNotEqual(update1, update2)
        self.assertEqual(dic2['my_name'], "Holberton")

    def test_basemodel1(self):
        '''Test for BaseModel'''
        dict1 = self.obj.to_dict()
        key = self.obj.__class__.__name__ + '.' + self.obj.id
        storage.save()
        with open("file.json", 'r') as f:
            dict2 = json.load(f)
        new = dict2[key]
        for k in new:
            self.assertEqual(dict1[k], new[k])

    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

if __name__ == "__main__":
    '''Main Initializer'''
    unittest.main()
