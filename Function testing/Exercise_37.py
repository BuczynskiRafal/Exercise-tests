import unittest
import math


def perimeter(radius):
    """The function returns the length of the circle."""

    if not (isinstance(radius, (int, float))):
        raise TypeError('The radius must be of type int or float.')

    if not radius > 0:
        raise ValueError('The radius must be positive.')

    return 2 * math.pi * radius


class TestPerimeter(unittest.TestCase):

    def test_value(self):
        self.assertRaises(ValueError, perimeter, -2)

    def test_type(self):
        self.assertRaises(TypeError, perimeter, 'str')

    def test_equal(self):
        self.assertAlmostEqual(perimeter(5), 31.4, 1)

    def test_greater_equal(self):
        self.assertGreaterEqual(perimeter(5), 30)

    def test_circle_perimeter_with_radius_one(self):
        self.assertAlmostEqual(perimeter(1), 6.28319, 5)

    def test_circle_perimeter_with_radius_three(self):
        self.assertAlmostEqual(perimeter(3), 18.84956, 5)

    def test_perimeter_incorrect_type_should_raise_type_error(self):
        self.assertRaises(TypeError, perimeter, '4')
        self.assertRaises(TypeError, perimeter, None)

    def test_perimeter_incorrect_value_should_raise_value_error(self):
        self.assertRaises(ValueError, perimeter, 0)
        self.assertRaises(ValueError, perimeter, -3)