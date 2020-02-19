#!/usr/bin/python3
'''Unittest Console Modules'''

import unittest
import pep8


def TestConsole(unittest.TestCase):
    '''Unittest for console'''

    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['console.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

if __name__ == '__main__':
    unittest.main()
