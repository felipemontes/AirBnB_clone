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
import os
import pep8


class TestFileStorage(unittest.TestCase):
    """ Test cases for FileStorage"""

    def setUp(self):
        """ remove the file """
        try:
            os.remove("file.json")
        except:
            pass
        FileStorage._FileStorage__objects = {}

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
        """ Test create User """
        obj = City()
        key = obj.__class__.__name__ + '.' + obj.id
        dic = {key: obj}
        self.assertEqual(storage.all(), dic)

    def test_create_amenity(self):
        """ Test create User """
        obj = Amenity()
        key = obj.__class__.__name__ + '.' + obj.id
        dic = {key: obj}
        self.assertEqual(storage.all(), dic)

    def test_create_place(self):
        """ Test create User """
        obj = Place()
        key = obj.__class__.__name__ + '.' + obj.id
        dic = {key: obj}
        self.assertEqual(storage.all(), dic)

    def test_create_review(self):
        """ Test create User """
        obj = Review()
        key = obj.__class__.__name__ + '.' + obj.id
        dic = {key: obj}
        self.assertEqual(storage.all(), dic)

    def test_create_state(self):
        """ Test create User """
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

    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")


if __name__ == "__main__":
    unittest.main()
