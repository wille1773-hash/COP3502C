#https://github.com/wille1773-hash/lab11-WE-MN.git
#Partner1: William Evans
#Partner2: Matthew Nunes
import math
"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
def square_root(a):
    if a < 0:
        raise ValueError("negative input")
    return math.sqrt(a)
def hypotenuse(a, b):
    return math.hypot(a, b)
def add(a, b): 
    return a + b
def subtract(a, b):
    return a - b
def mul(a, b):
    return a * b
def div(a,b):
    if b == 0:
        raise ZeroDivisionError
    return a / b
def logarithm(a, b):
    if a <= 0 or a == 1  or b <= 0:
        raise ValueError("invalid base or argument for logarithm")
    return math.log(b, a)
def exp(a, b):
    return a ** b
