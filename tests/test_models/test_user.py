#!/usr/bin/python3
'''Unittest User Module'''
import unittest
from models.user import User
import datetime
import pep8


class TestUser(unittest.TestCase):
    '''Unittests for User'''
    u = User()

    def test_exist(self):
        '''Check if class exists'''
        self.assertEqual(str(type(self.u)), "<class 'models.user.User'>")

    def test_inheritance(self):
        '''Check inheritance'''
        self.assertIsInstance(self.u, User)

    def test_pep8_conformance(self):
        '''Test that we conform to PEP8.'''
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/user.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

if __name__ == '__main__':
    '''Main initializer'''
    unittest.main()
