import unittest
from solution_exercise_91 import is_distinct


class TestIsDistinct(unittest.TestCase):

    def test_is_distinct_empty_list(self):
        msg = 'Popraw implementację funkcji is_distinct().'
        self.assertEqual(is_distinct([]), True, msg)

    def test_is_distinct_with_numbers_should_return_false(self):
        msg = 'Popraw implementację funkcji is_distinct().'
        self.assertEqual(is_distinct([3, 3, 1]), False, msg)

    def test_is_distinct_with_numbers_should_return_true(self):
        msg = 'Popraw implementację funkcji is_distinct().'
        self.assertEqual(is_distinct([3, 2, 1]), True, msg)

    def test_is_distinct_with_strings(self):
        msg = 'Popraw implementację funkcji is_distinct().'
        self.assertEqual(is_distinct(['c++', 'c', 'r']), True, msg)