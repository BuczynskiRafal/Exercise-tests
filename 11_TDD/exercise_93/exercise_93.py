import unittest
from solution_exercise_93 import Laptop


class TestLaptop(unittest.TestCase):

    def setUp(self):
        self.laptop = Laptop('Acer', 'Predator', 5490)

    def test_laptop_has_brand_instance_attr(self):
        msg = 'Brak atrybutu instancji brand.'
        self.assertTrue(hasattr(self.laptop, 'brand'), msg)

    def test_laptop_has_model_instance_attr(self):
        msg = 'Brak atrybutu instancji model.'
        self.assertTrue(hasattr(self.laptop, 'model'), msg)

    def test_laptop_has_price_instance_attr(self):
        msg = 'Brak atrybutu instancji price.'
        self.assertTrue(hasattr(self.laptop, 'price'), msg)

    def test_laptop_has_three_instance_attrs(self):
        msg = 'Nie zdefiniowano dokładnie trzech atrybutów instancji.'
        actual = len([attr for attr in dir(self.laptop)
                      if not attr.startswith('_')])
        expected = 3
        self.assertEqual(actual, expected, msg)