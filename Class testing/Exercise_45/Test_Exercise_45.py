import unittest
from Exercise_45 import *


class TestEmployee(unittest.TestCase):

    emp = Employee('John', 'Smith', 40, 80000)

    def test_email(self):
        self.assertEqual(self.emp.email, 'john.smith@mail.com')