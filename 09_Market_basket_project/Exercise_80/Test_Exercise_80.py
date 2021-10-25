import unittest
from Exercise_80 import *
from basket import *


class TestBasketWithNoProduct(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print('setting up')
        cls.basket = ShoppingBasket()

    def test_size_of_basket_should_be_empty(self):
        self.assertEqual(self.basket.__len__(), 0)

    def test_getting_product_out_of_range_should_raise_error(self):
        self.assertRaises(IndexError, self.basket.get_product, 0)

    def test_total_amount_should_be_zero(self):
        self.assertEqual(self.basket.total(), 0)
