import unittest
from solution_exercise_101 import Vector


class TestVector(unittest.TestCase):

    def setUp(self):
        self.v = Vector(-3, 4, 2)
        self.w = Vector(1, -3)

    def test_vector_repr_method(self):
        msg = 'Popraw implementację metody __repr__().'
        self.assertEqual(repr(self.v), "Vector(-3, 4, 2)", msg)
        self.assertEqual(repr(self.w), "Vector(1, -3)", msg)

    def test_vector_len_method(self):
        msg = 'Popraw implementację metody __len__().'
        self.assertEqual(len(self.v), 3, msg)
        self.assertEqual(len(self.w), 2, msg)