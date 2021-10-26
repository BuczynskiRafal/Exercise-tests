import unittest
from solution_exercise_89 import count_string


class TestCountString(unittest.TestCase):

    def test_count_string_empty_list(self):
        msg = 'Popraw implementację funkcji count_string().'
        self.assertEqual(count_string([]), 0, msg)

    def test_count_string_without_string(self):
        msg = 'Popraw implementację funkcji count_string().'
        self.assertEqual(count_string([1, 2]), 0, msg)

    def test_count_string_with_three_string(self):
        msg = 'Popraw implementację funkcji count_string().'
        self.assertEqual(count_string(['c++', 3, 'c', 'java']), 3, msg)