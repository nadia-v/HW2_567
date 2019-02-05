# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def test_classifyTriangle(self): 

        #Testing expected output
        self.assertEqual(classifyTriangle(5, 8, 12), 'Scalene')     #Testing scalene triangle 
        self.assertEqual(classifyTriangle(23456, 23456, 19876),'Isosceles')     #Testing isosceles triangle / large number
        self.assertEqual(classifyTriangle(1, 1, 1),'Equilateral')     #Testing equilateral triangle 
        self.assertEqual(classifyTriangle(3, 4, 5),'Right, Scalene')   #Testing right, scalene triangle 
        self.assertEqual(classifyTriangle(0.5, 0.3, 0.4),'Right, Scalene')   #Testing right, scalene triangle / float
        self.assertEqual(classifyTriangle(2, 2, (8 ** 0.5)),'Right, Isosceles')   #Testing right, isosceles triangle 
        self.assertEqual(classifyTriangle(2, (8 ** 0.5), 2),'Right, Isosceles')   #Testing right, isosceles triangle 
        #Testing invalid input
        self.assertEqual(classifyTriangle('five', 8, 12), 'InvalidInput')    #Type error
        self.assertEqual(classifyTriangle(6, 8, '@'), 'InvalidInput')    #Type error
        self.assertEqual(classifyTriangle(6, 8, 0), 'InvalidInput')    #Zero
        self.assertEqual(classifyTriangle(0, 0, 0), 'InvalidInput')    #All zeros
        self.assertEqual(classifyTriangle(6, 1, 2), 'InvalidInput')    #Side larger than the sum of other two
        self.assertEqual(classifyTriangle(6, 4, 2), 'InvalidInput')    #Side equal to the sum of other two
        self.assertEqual(classifyTriangle(6, 8, -4), 'InvalidInput')    #Negative number
        self.assertEqual(classifyTriangle(-3, -4, -5), 'InvalidInput')    #All negative numbers

        #Testing unexpected output
        self.assertNotEqual(classifyTriangle(5, 8, 12), 'Right, Isosceles')
        self.assertNotEqual(classifyTriangle(23456, 23456, 19876),'Scalene')    
        self.assertNotEqual(classifyTriangle(1, 1, 1),'Scalene')     
        self.assertNotEqual(classifyTriangle(3, 4, 5),'Scalene')   
        self.assertNotEqual(classifyTriangle(0.5, 0.3, 0.4),'Right, Isosceles')   
        self.assertNotEqual(classifyTriangle(2, 2, (8 ** 0.5)),'Isosceles')   
        self.assertNotEqual(classifyTriangle(2, (8 ** 0.5), 2),'Right, Scalene')   


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

