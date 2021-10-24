import unittest
from Exercise_47 import Employee


class TestEmployee(unittest.TestCase):

    def test_email(self):
        emp = Employee('John', 'Smith', 40, 80000)
        self.assertEqual(emp.email, 'john.smith@mail.com')

    def test_email_after_changing_first_name(self):
        emp = Employee('John', 'Smith', 40, 80000)
        emp.first_name = 'Mike'
        self.assertEqual(emp.email, 'mike.smith@mail.com')

    def test_email_after_changing_last_name(self):
        emp = Employee('John', 'Smith', 40, 80000)
        emp.last_name = 'Doe'
        self.assertEqual(emp.email, 'john.doe@mail.com')