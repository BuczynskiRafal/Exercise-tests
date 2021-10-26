import unittest
from solution_exercise_94 import Laptop


class TestLaptop(unittest.TestCase):

    def test_laptop_incorrect_price_should_raise_type_error(self):
        self.assertRaises(TypeError, Laptop, 'Acer', 'Predator', 'thousand')
        self.assertRaises(TypeError, Laptop, 'Acer', 'Predator', [2000])
        self.assertRaises(TypeError, Laptop, 'Acer', 'Predator', None)