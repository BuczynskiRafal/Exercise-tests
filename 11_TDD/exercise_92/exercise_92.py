import unittest
from solution_exercise_92 import Phone


class TestPhone(unittest.TestCase):

    def test_brand_attr(self):
        msg = 'Brak atrybutu brand klasy Phone.'
        self.assertTrue(hasattr(Phone, 'brand'), msg)

    def test_model_attr(self):
        msg = 'Brak atrybutu model klasy Phone.'
        self.assertTrue(hasattr(Phone, 'model'), msg)

    def test_check_user_defined_class_attr(self):
        msg = 'Nie zdefiniowano dokładnie dwóch atrybutów klasy Phone.'
        actual = len([attr for attr in dir(Phone) if not attr.startswith('_')])
        expected = 2
        self.assertEqual(actual, expected, msg)