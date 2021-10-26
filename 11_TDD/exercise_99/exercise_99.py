import unittest
from solution_exercise_99 import Person


class TestPerson(unittest.TestCase):

    def setUp(self):
        self.person = Person('John', 'Smith')

    def test_person_repr_method(self):
        msg = 'Popraw implementację metody __repr__().'
        actual = repr(self.person)
        expected = "Person(fname='John', lname='Smith')"
        self.assertEqual(actual, expected, msg)