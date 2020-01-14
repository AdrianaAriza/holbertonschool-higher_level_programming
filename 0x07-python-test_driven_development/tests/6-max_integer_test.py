#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

        def test(self):
                self.assertEqual(max_integer([-1, 2, 3, 4]), 4)
                self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
                self.assertEqual(max_integer([]), None)
                self.assertEqual(max_integer("hola"), 'o')
        def test1(self):
                with self.assertRaises(TypeError):
                        max_integer([3, "HOLA"])
        def test2(self):
                with self.assertRaises(TypeError):
                        max_integer(5)

if __name__ == '__main__':
        unittest.main()
