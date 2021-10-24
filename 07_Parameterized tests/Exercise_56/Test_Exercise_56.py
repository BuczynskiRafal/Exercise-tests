import unittest
from Exercise_56 import calc_tax


class TestCalcTax(unittest.TestCase):

    def test_calc_tax(self):
        casus1 = (60000, 0.2, 18, 5000)
        casus2 = (60000, 0.2, 19, 12000)
        casus3 = (60000, 0.2, 65, 12000)
        casus4 = (60000, 0.2, 66, 8000)
        cases = [casus1, casus2, casus3, casus4]

        for amount, tax_rate, age, result in cases:
            with self.subTest(cases=cases):
                self.assertEqual(calc_tax(amount, tax_rate, age), result)
