#!/usr/bin/python3
""" Unittest for State """

import unittest
import pep8
from models.base_model import BaseModel
from models.state import State


class TestAmenity(unittest.TestCase):
    """ """
    def test_pep8(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/amenity.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")
