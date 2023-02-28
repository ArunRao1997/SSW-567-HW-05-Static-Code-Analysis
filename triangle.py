# -*- coding: utf-8 -*-
"""
Created on Feb 28, 2023
The primary goal of this module is to provide a function to classify triangles.
"""


def classify_triangle(side_a, side_b, side_c):
    """
    This function takes three side lengths as inputs and returns a string describing
    the type of triangle that they form: equilateral, isosceles, scalene, or right.
    """
    result = ''
    sides = [side_a, side_b, side_c]
    sides.sort()
    if not (isinstance(side_a, (int, float))
            and isinstance(side_b, (int, float))
            and isinstance(side_c, (int, float))):
        result = 'InvalidInput'
    elif side_a >= 200 or side_b >= 200 or side_c >= 200:
        result = 'InvalidInput'
    elif side_a <= 0 or side_b <= 0 or side_c <= 0:
        result = 'InvalidInput'
    elif sides[0] + sides[1] <= sides[2]:
        result = 'NotATriangle'
    elif side_a == side_b == side_c:
        result = 'Equilateral'
    elif sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2:
        result = 'Right and Scalene'
    elif side_a == side_b or side_b == side_c or side_c == side_a:
        result = 'Isosceles'
    else:
        result = 'Scalene'
    return result
