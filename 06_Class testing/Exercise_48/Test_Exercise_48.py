import unittest
from Exercise_48 import Employee


class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.emp = Employee('John', 'Smith', 40, 80000)

    def test_email(self):
        emp = Employee('John', 'Smith', 40, 80000)
        self.assertEqual(emp.email, 'john.smith@mail.com')

    def test_email_after_changing_first_name(self):
        self.emp.first_name = 'Mike'
        self.assertEqual(self.emp.email, 'mike.smith@mail.com')

    def test_email_after_changing_last_name(self):
        self.emp.last_name = 'Doe'
        self.assertEqual(self.emp.email, 'john.doe@mail.com')