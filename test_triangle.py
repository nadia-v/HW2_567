# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from triangle import classify_triangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def test_classify_triangle(self):

        #Testing expected output
        self.assertEqual(classify_triangle(5, 8, 12), 'Scalene')     #Testing scalene triangle
        self.assertEqual(classify_triangle(23456, 23456, 19876),'Isosceles')     #Testing isosceles triangle / large number
        self.assertEqual(classify_triangle(1, 1, 1),'Equilateral')     #Testing equilateral triangle
        self.assertEqual(classify_triangle(3, 4, 5),'Right, Scalene')   #Testing right, scalene triangle
        self.assertEqual(classify_triangle(0.5, 0.3, 0.4),'Right, Scalene')   #Testing right, scalene triangle / float


        #Testing invalid input
        self.assertRaises(ValueError, classify_triangle, 'five', 8, 12)     #Type error
        self.assertRaises(ValueError, classify_triangle, 6, 8, '@')     #Type error
        self.assertRaises(ValueError, classify_triangle, 6, 'zero', 6)     #Type error
        self.assertRaises(ValueError, classify_triangle, 6, 8, 0)     #Zero
        self.assertRaises(ValueError, classify_triangle, 0, 0, 0)     #All zeros
        self.assertRaises(ValueError, classify_triangle, 6, 1, 2)     #Side larger than the sum of other two
        self.assertRaises(ValueError, classify_triangle, 6, 4, 2)     #Side larger than the sum of other two
        self.assertRaises(ValueError, classify_triangle, 6, 8, -4)     #Negative number
        self.assertRaises(ValueError, classify_triangle, -3, -4, -5)     #All negative numbers
        with self.assertRaises(ValueError):     #catching exception
            classify_triangle('cat', 8, 8)
        with self.assertRaises(ValueError):     #catching exception
            classify_triangle(8, 8, 0)
        with self.assertRaises(ValueError):     #catching exception
            classify_triangle(16, 8, 8)

        #Testing unexpected output
        self.assertNotEqual(classify_triangle(5, 8, 12), 'Right, Isosceles')
        self.assertNotEqual(classify_triangle(23456, 23456, 19876),'Scalene')
        self.assertNotEqual(classify_triangle(1, 1, 1),'Scalene')
        self.assertNotEqual(classify_triangle(3, 4, 5),'Scalene')
        self.assertNotEqual(classify_triangle(0.5, 0.3, 0.4),'Right, Isosceles')




if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

