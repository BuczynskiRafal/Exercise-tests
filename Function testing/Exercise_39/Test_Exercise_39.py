import unittest
from Exercise_39 import calculate_tax


class TestCalculateTax(unittest.TestCase):

    def test_tax_twenty_percent_with_eighteen_age(self):
        self.assertEqual(calculate_tax(60000, 18, 20), 6000)

    def test_tax_twenty_percent_with_nineteen_age(self):
        self.assertEqual(calculate_tax(60000, 19, 20), 12000)

    def test_tax_twenty_percent_with_sixty_five_age(self):
        self.assertEqual(calculate_tax(60000, 65, 20), 12000)

    def test_tax_twenty_percent_with_sixty_six_age(self):
        self.assertEqual(calculate_tax(60000, 66, 20), 9000)
