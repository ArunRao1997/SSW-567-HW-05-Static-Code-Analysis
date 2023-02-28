# -*- coding: utf-8 -*-
"""
Created on Feb 4, 2023

The primary goal of this file is to demonstrate a simple python program to classify triangles

@author: Arun Rao Nayineni
"""
from MyBrand import my_brand

def classifyTriangle(a, b, c):
    # verify that all 3 inputs are integers
    # Python's "isinstance(object,type) returns True if the object is of the specified type
    if not (isinstance(a, int) and isinstance(b, int) and isinstance(c, int)):
        return 'InvalidInput';

    # require that the input values be >= 0 and <= 200
    if a >= 200 or b >= 200 or c >= 200:
        return 'InvalidInput'

    if a <= 0 or b <= 0 or c <= 0:
        return 'InvalidInput'

    # This information was not in the requirements spec but
    # is important for correctness
    # the sum of any two sides must be strictly less than the third side
    # of the specified shape is not a triangle
    if (a + b <= c) or (a + c <= b) or (b + c <= a):
        return 'NotATriangle'

    # now we know that we have a valid triangle
    if a == b and b == c and c == a:
        return 'Equilateral'
    elif ((a ** 2) + (b ** 2)) == (c ** 2) or ((b ** 2) + (c ** 2)) == (a ** 2) or ((c ** 2) + (a ** 2)) == (
            b ** 2):  # Validating if it's Right
        if a != b != c:  # Right and Scalene
            return 'Right angle and Scalene'
        if (a == b) or (b == c) or (c == a):  # Right and Isosceles
            return 'Right angle and Isosceles'
        return 'Right angle'  # else just right
    elif (a == b) or (b == c) or (c == a):  # If it's Isosceles
        return 'Isosceles'
    else:
        return 'Scalene'


print(classifyTriangle(3, 4, 5))  # printing to check output
