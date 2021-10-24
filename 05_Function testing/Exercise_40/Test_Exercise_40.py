import unittest
from Exercise_40 import income_tax


class TestIncomeTax(unittest.TestCase):

    def test_tax_below_threshold(self):
        self.assertAlmostEqual(income_tax(60000), 10200)

    def test_tax_equal_threshold(self):
        self.assertAlmostEqual(income_tax(85528), 14539.76)

    def test_tax_above_threshold(self):
        self.assertAlmostEqual(income_tax(100000), 19170.8)