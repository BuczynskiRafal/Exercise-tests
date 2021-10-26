import unittest
from solution_exercise_88 import factorial


class TestFactorial(unittest.TestCase):

    def test_factorial(self):
        msg = 'Popraw implementację funkcji factorial().'
        self.assertEqual(factorial(0), 1, msg)
        self.assertEqual(factorial(1), 1, msg)
        self.assertEqual(factorial(2), 2, msg)
        self.assertEqual(factorial(3), 6, msg)
        self.assertEqual(factorial(6), 720, msg)