#https://github.com/wille1773-hash/lab11-WE-MN.git
#Partner1: William Evans
#Partner2: Matthew Nunes
import sys, os
sys.path.append(os.path.dirname(__file__))
import unittest
from calculator import *
import math
import calculator

class TestCalculator(unittest.TestCase):
    ######## Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(calculator.add(2,2),4)
        self.assertEqual(calculator.add(12,73),85)
        self.assertEqual(calculator.add(1,9),10)


    def test_subtract(self): # 3 assertions
        self.assertEqual(calculator.subtract(10,5),5)
        self.assertEqual(calculator.subtract(100,5),95)
        self.assertEqual(calculator.subtract(2,1),1)


    ##########################

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(calculator.mul(2, 3), 6)
        self.assertEqual(calculator.mul(-2, 3), -6)
        self.assertEqual(calculator.mul(0, 5), 0)

    def test_divide(self): # 3 assertions
        self.assertEqual(calculator.div(4,2), 2)
        self.assertEqual(calculator.div(10, 2), 5)
        self.assertEqual(calculator.div(10, -2), -5)
        with self.assertRaises(ZeroDivisionError):
            calculator.div(10, 0)
    # ##########################

    ####### Partner 2
    def test_divide_by_zero(self): # 1 assertion
        # call division function inside, example:
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #     div(0, 5)
        with self.assertRaises(ZeroDivisionError):
            calculator.div(10,0)

    def test_logarithm(self): # 3 assertions
        self.assertEqual(calculator.logarithm(2,4), math.log(4,2))
        self.assertEqual(calculator.logarithm(10,100), math.log(100,10))
        self.assertEqual(calculator.logarithm(2,16), math.log(16,2))


    def test_log_invalid_base(self): # 1 assertion
        # use same technique from test_divide_by_zero
        with self.assertRaises(ValueError):
            calculator.logarithm(1,17)
    ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            calculator.logarithm(2, -8)

    def test_hypotenuse(self):
        self.assertAlmostEqual(calculator.hypotenuse(3, 4), 5.0)
        self.assertAlmostEqual(calculator.hypotenuse(5, 12), 13.0)

    def test_sqrt(self):
        self.assertAlmostEqual(calculator.square_root(4), 2.0)
        self.assertAlmostEqual(calculator.square_root(9), 3.0)
        with self.assertRaises(ValueError):
            calculator.square_root(-1)

# Do not touch this
if __name__ == "__main__":
    unittest.main()