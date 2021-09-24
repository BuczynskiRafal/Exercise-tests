import unittest
import math


def area(radius):
    """The function returns the area of the circle."""

    if not (isinstance(radius, (int, float))):
        raise TypeError('The radius must be of type int or float.')

    if not radius > 0:
        raise ValueError('The radius must be positive.')

    return math.pi * radius ** 2


class TestArea(unittest.TestCase):

    def test_circle_area_with_radius_one(self):
        self.assertAlmostEqual(area(1), 3.14159, 5)

    def test_circle_area_with_radius_three(self):
        self.assertAlmostEqual(area(3), 28.27433, 5)

    def test_area_incorrect_type_should_raise_type_error(self):
        self.assertRaises(TypeError, area, '4')
        self.assertRaises(TypeError, area, None)

    def test_area_incorrect_value_should_raise_value_error(self):
        self.assertRaises(ValueError, area, 0)
        self.assertRaises(ValueError, area, -3)