import unittest
from Exercise_55 import calc_tax


class TestCalcTax(unittest.TestCase):

    def test_calc_tax_twenty_percent_and_eighteen_age(self):
        self.assertEqual(calc_tax(60000, 0.2, 18), 5000)

    def test_calc_tax_twenty_percent_and_nineteen_age(self):
        self.assertEqual(calc_tax(60000, 0.2, 19), 12000)

    def test_calc_tax_twenty_percent_and_sixty_five_age(self):
        self.assertEqual(calc_tax(60000, 0.2, 65), 12000)

    def test_calc_tax_twenty_percent_and_sixty_six_age(self):
        self.assertEqual(calc_tax(60000, 0.2, 66), 8000)