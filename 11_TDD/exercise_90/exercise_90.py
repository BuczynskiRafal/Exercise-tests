import unittest
from solution_exercise_90 import remove_duplicates


class TestRemoveDuplicates(unittest.TestCase):

    def test_remove_duplicates_empty_list(self):
        msg = 'Popraw implementację funkcji remove_duplicates().'
        self.assertEqual(remove_duplicates([]), [], msg)

    def test_remove_duplicates_without_string(self):
        msg = 'Popraw implementację funkcji remove_duplicates().'
        self.assertEqual(remove_duplicates([3, 3, 1]), [1, 3], msg)

    def test_remove_duplicates_with_three_string(self):
        msg = 'Popraw implementację funkcji remove_duplicates().'
        actual = sorted(remove_duplicates(['c++', 'c', 'c']))
        expected = ['c', 'c++']
        self.assertEqual(actual, expected, msg)