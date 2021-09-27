import unittest
from Exercise_38 import calculate_tax


class TestCalculateTax(unittest.TestCase):

    def test_tax_with_eighteen_age(self):
        self.assertEqual(calculate_tax(60000, 18, 17), 6000)

    def test_tax_with_nineteen_age(self):
        self.assertEqual(calculate_tax(60000, 19, 17), 10200)

    def test_tax_with_sixty_five_age(self):
        self.assertEqual(calculate_tax(60000, 65, 17), 10200)

    def test_tax_with_sixty_six_age(self):
        self.assertEqual(calculate_tax(60000, 66, 17), 9000)
