import unittest
from Exercise_41 import SimpleTaxCalculator


class TestIncomeTax(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.calc = SimpleTaxCalculator()

    def test_income_below_threshold(self):
        self.assertEqual(self.calc.income_tax(60000), 10200)

    def test_income_equal_threshold(self):
        self.assertEqual(self.calc.income_tax(85528), 14539.76)

    def test_income_above_threshold(self):
        self.assertEqual(self.calc.income_tax(100000), 19170.8)
