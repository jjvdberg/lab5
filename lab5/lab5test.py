#!/usr/bin/python3

import unittest
import lab5a
import lab5b
import lab5c

class lab5Test(unittest.TestCase):
    
    def testSum(self):
        self.assertEqual(lab5a.sum(4, 5), 9, "Sum failed the test")
    
    def testProduct(self):
        self.assertEqual(lab5b.product(4, 5), 20, "Product failed the test")

    def testLab5c(self):
        testTriangle = lab5c.Triangle(3, 4, 5)
        
        heigth = 2 * (3 / 4)
        area = (heigth * 5) / 2
        
        self.assertEqual(testTriangle.height(), heigth, "Triangle Heigth failed the test")
        self.assertEqual(testTriangle.area(), area, "Triangle area failed the test")