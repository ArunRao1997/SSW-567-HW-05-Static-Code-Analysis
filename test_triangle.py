"""
Updated Feb 28, 2023
The primary goal of this file is to demonstrate a simple unittest implementation.

Author: Arun Rao Nayineni
"""

import math
import unittest
from triangle import classify_triangle


class TestTriangles(unittest.TestCase):
    """This class contains unit tests for `classify_triangle` function."""

    def test_right_triangle_a(self):
        """Tests if the function can correctly identify a right and scalene triangle."""
        self.assertEqual(classify_triangle(3, 4, 5), 'Right and Scalene',
                         '3,4,5 is a Right angle and scalene triangle')

    def test_right_triangle_and_scalene(self):
        """Tests if the function can correctly identify a right and scalene triangle."""
        self.assertEqual(classify_triangle(8, 6, 10), 'Right and Scalene',
                         '8,6,10 is a Right angle and scalene triangle')

    def test_equilateral_triangle_a(self):
        """Tests if the function can correctly identify an equilateral triangle."""
        self.assertEqual(classify_triangle(1, 1, 1), 'Equilateral', '1,1,1 should be equilateral')

    def test_equilateral_triangle_b(self):
        """Tests if the function can correctly identify an equilateral triangle."""
        self.assertEqual(classify_triangle(7, 7, 7), 'Equilateral', '7,7,7 is equilateral')

    def test_scalene_triangle_a(self):
        """Tests if the function can correctly identify a scalene triangle."""
        self.assertEqual(classify_triangle(3, 4, 6), 'Scalene', '10,11,12 is Scalene')

    def test_scalene_triangle_b(self):
        """Tests if the function can correctly identify a scalene triangle."""
        self.assertEqual(classify_triangle(100, 110, 112), 'Scalene', '100,110,112 is Scalene')

    def test_isosceles_triangle_a(self):
        """Tests if the function can correctly identify an isosceles triangle."""
        self.assertEqual(classify_triangle(5, 5, 3), 'Isosceles', '5,5,3 is Isosceles')

    def test_isosceles_triangle_b(self):
        """Tests if the function can correctly identify an isosceles triangle."""
        self.assertEqual(classify_triangle(4, 6, 6), 'Isosceles', '4,6,6 is Isosceles')

    def test_isosceles_triangle_c(self):
        """Tests if the function can correctly identify an isosceles triangle."""
        self.assertEqual(classify_triangle(8, 6, 8), 'Isosceles', '8,6,8 is Isosceles')

    def test_isosceles_triangle_d(self):
        """Tests if the function can correctly identify an isosceles triangle."""
        self.assertEqual(classify_triangle(6, 6, 4), 'Isosceles', '6,6,4 is Isosceles')

    def test_invalid_input1(self):
        """Tests if the function can correctly identify invalid inputs."""
        self.assertEqual(classify_triangle(-1, -1, -1), 'InvalidInput', 'InvalidInput')
        self.assertEqual(classify_triangle(0, 0, 0), 'InvalidInput', 'InvalidInput')
        self.assertEqual(classify_triangle(2, -5, math.sqrt(2)), 'InvalidInput')

    def test_invalid_input_2(self):
        """
        Test that classify_triangle returns 'InvalidInput' when all sides are greater than 200
        """
        self.assertEqual(classify_triangle(201, 201, 201), 'InvalidInput', 'InvalidInput')

    def test_invalid_input_3(self):
        """
        Test that classify_triangle returns 'InvalidInput' when sides are not integers
        """
        self.assertEqual(classify_triangle("200", "200", "200"), 'InvalidInput', 'InvalidInput')

    def test_not_a_triangle_1(self):
        """
        Test that classify_triangle returns 'NotATriangle'
        when the sum of two sides is less than or equal to the third side
        """
        self.assertEqual(classify_triangle(1, 3, 5), 'NotATriangle', '1,3,5 is NotATriangle')

    def test_not_a_triangle_2(self):
        """
        Test that classify_triangle returns 'NotATriangle'
         when the sum of two sides is less than or equal to the third side
        """
        self.assertEqual(classify_triangle(1, 4, 5), 'NotATriangle', '1,4,5 is NotATriangle')

    def test_not_a_triangle_3(self):
        """
        Test that classify_triangle returns 'NotATriangle'
        when the sum of two sides is less than or equal to the third side
        """
        self.assertEqual(classify_triangle(1, 17, 5), 'NotATriangle', '1,17,5 is NotATriangle')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()  # Invoking function calls via main
