#!/usr/bin/python3
"""Unittest for max_integer([..])
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_max_int(self):
        """Test various real number instances"""
        self.assertEqual(max_integer([3, 5, 7, 9]), 9)
        self.assertEqual(max_integer([-3, 5, -7, -9]), 5)
        self.assertEqual(max_integer([0, 0, 0, 0]), 0)
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_beginning(self):
        """Test max integer at beginning"""
        self.assertEqual(max_integer([5, 4, 3, 2]), 5)

    def test_floats(self):
        """ Tests a list of float numbers."""
        self.assertEqual(max_integer([1.53, 6.33, -9.123, 15.2, 6.0]), 15.2)

    def test_one_element_list(self):
        """One element list"""
        self.assertEqual(max_integer([8]), 8)

    def test_string(self):
        """Test String."""
        self.assertEqual(max_integer("abcz"), "z")

    def test_list_strings(self):
        strings = ["Python", "is", "fun", "for", "Jeffrey"]
        self.assertEqual(max_integer(strings), "is")

    def test_empty_string(self):
        """Test an empty string."""
        self.assertEqual(max_integer(""), None)

    if __name__ == '__main__':
        unittest.main()
