#!/usr/bin/python3
'''Unittest User Module'''
import unittest
from models.user import User
import datetime


class TestUser(unittest.TestCase):
    '''Unittests for User'''
    u = User()

    def test_exist(self):
        '''Check if class exists'''
        self.assertEqual(str(type(self.u)), "<class 'models.user.User'>")

    def test_inheritance(self):
        '''Check inheritance'''
        self.assertIsInstance(self.u, User)

if __name__ == '__main__':
    '''Main initializer'''
    unittest.main()
