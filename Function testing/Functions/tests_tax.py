import unittest
from tax import calc_tax


class TestTax(unittest.TestCase):

    def test_calc_tax_negative_age_should_raise_error(self):
        self.assertRaises(ValueError, calc_tax, 60000, 0.20, -10)

    def test_calc_tax_negative_tax_rate_should_raise_error(self):
        self.assertRaises(ValueError, calc_tax, 60000, -0.20, 10)

    def test_calc_tax_negative_amount_should_raise_error(self):
        self.assertRaises(ValueError, calc_tax, -60000, 0.20, 10)

    def test_calc_tax_incorrect_age_type(self):
        self.assertRaises(TypeError, calc_tax, 60000, 0.20, '10')

    def test_calc_tax_incorrect_amount_type(self):
        self.assertRaises(TypeError, calc_tax, '60000', 0.20, 10)

    def test_calc_tax_incorrect_tax_rate_type(self):
        self.assertRaises(TypeError, calc_tax, 60000, '0.20', 10)

    def test_calc_tax(self):
        self.assertEqual(calc_tax(60000, 0.20, 10), 5000)
        self.assertAlmostEqual(calc_tax(60000, 0.20, 10), 5000)

    def test_calc_tax_eighteen_age_and_below(self):
        self.assertEqual(calc_tax(60000, 0.2, 18), 5000)
        self.assertEqual(calc_tax(25000, 0.2, 18), 5000)
        self.assertLessEqual(calc_tax(20000, 0.2, 18), 5000)

    def test_calc_tax_sixty_five_age_above(self):
        self.assertEqual(calc_tax(60000, 0.20, 66), 8000)
        self.assertEqual(calc_tax(60000, 0.20, 65), 12000)
        self.assertLessEqual(calc_tax(35000, 0.20, 65), 12000)

    def test_calc_tax_between_18_and_65_age(self):
        self.assertEqual(calc_tax(60000, 0.2, 30), 12000)
        self.assertGreaterEqual(calc_tax(60000, 0.2, 30), 5000)
        self.assertGreaterEqual(calc_tax(60000, 0.2, 30), 8000)