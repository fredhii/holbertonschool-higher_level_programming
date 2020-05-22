#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """ Unit test class """
    def test_ten_scale(self):
        l  = [10, 20, 30, 40]
        self.assertEqual(max_integer(l), 40)

    def test_negative_charge(self):
        l  = [-23, -48, -13, -7]
        self.assertEqual(max_integer(l), -7)

    def test_alone(self):
        l  = [7]
        self.assertEqual(max_integer(l), 7)

    def test_none(self):
        l = []
        self.assertEqual(max_integer(l), None)

    def test_float_charge(self):
        l = [1.0, 2.0, 3.0, 7.0]
        self.assertEqual(max_integer(l), 7.0)

    def test_two_max_numbers(self):
        l = [1, 2, 3, 7, 5, 7]
        self.assertEqual(max_integer(l), 7)

    def test_string(self):
        l = "testify"
        self.assertEqual(max_integer(l), 'y')

    def test_mix_list(self):
        l = ['T', 7, 3.0]
        with self.assertRaises(TypeError):
            max_integer(l)

if __name__ == '__main__':
    unittest.main()
