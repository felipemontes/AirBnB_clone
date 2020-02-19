#!/usr/bin/python3
""" Unittest for Storage """
import unittest
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import os


class TestFileStorage(unittest.TestCase):
    """ Test cases for FileStorage"""

    def setUp(self):
        """ remove the file """
        try:
            os.remove("file.json")
        except:
            pass
        FileStorage._FileStorage__objects = {}

    def test_empty(self):
        """ Test empty file """
        self.assertEqual(storage.all(), {})

    def test_create_basemodel(self):
        """ Test create basemodel"""
        obj = BaseModel()
        name = obj.__class__.__name__ + '.' + obj.id
        dic = {name: obj}
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


if __name__ = "__main__":
    unittest.main()
