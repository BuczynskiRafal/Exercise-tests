import unittest
from solution_exercise_87 import filter_ge_four_char


class TestFilterGeFourChar(unittest.TestCase):

    def test_filter_ge_four_char_with_one_item(self):
        msg = 'Popraw implementację funkcji filter_ge_four_char().'
        actual = filter_ge_four_char(['sql', 'r', 'java'])
        expected = ['java']
        self.assertEqual(actual, expected, msg)

    def test_filter_ge_four_char_with_two_item(self):
        msg = 'Popraw implementację funkcji filter_ge_four_char().'
        actual = filter_ge_four_char(['sql', 'r', 'python', 'java'])
        expected = ['python', 'java']
        self.assertEqual(actual, expected, msg)

    def test_filter_ge_four_char_should_be_empty(self):
        msg = 'Popraw implementację funkcji filter_ge_four_char().'
        actual = filter_ge_four_char([])
        expected = []
        self.assertEqual(actual, expected, msg)