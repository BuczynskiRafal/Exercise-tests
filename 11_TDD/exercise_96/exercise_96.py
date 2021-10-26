import unittest
from solution_exercise_96 import Laptop


class TestLaptop(unittest.TestCase):

    def test_laptop_incorrect_brand_should_raise_type_error(self):
        self.assertRaises(TypeError, Laptop, 200, 'Predator', 1000)
        self.assertRaises(TypeError, Laptop, True, 'Predator', 1000)

    def test_laptop_incorrect_price_should_raise_type_error(self):
        self.assertRaises(TypeError, Laptop, 'Acer', 'Predator', 'thousand')
        self.assertRaises(TypeError, Laptop, 'Acer', 'Predator', [2000])
        self.assertRaises(TypeError, Laptop, 'Acer', 'Predator', None)

    def test_laptop_incorrect_price_should_raise_value_error(self):
        self.assertRaises(ValueError, Laptop, 'Acer', 'Predator', -1000)
        self.assertRaises(ValueError, Laptop, 'Acer', 'Predator', 0)
