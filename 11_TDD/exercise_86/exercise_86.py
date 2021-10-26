import unittest
from solution_exercise_86 import map_longest


class TestMapLongest(unittest.TestCase):

    def test_map_longest_should_be_six(self):
        msg = 'Popraw implementację funkcji map_longest().'
        self.assertEqual(map_longest(['sql', 'r', 'python']), 6, msg)

    def test_map_longest_should_be_three(self):
        msg = 'Popraw implementację funkcji map_longest().'
        self.assertEqual(map_longest(['sql', 'r']), 3, msg)

    def test_map_longest_should_be_zero(self):
        msg = 'Popraw implementację funkcji map_longest().'
        self.assertEqual(map_longest([]), 0, msg)