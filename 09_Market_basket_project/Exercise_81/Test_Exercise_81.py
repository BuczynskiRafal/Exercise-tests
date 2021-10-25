import unittest
from basket import ShoppingBasket


class TestBasketWithNoProducts(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.basket = ShoppingBasket()

    def test_size_of_basket_should_be_empty(self):
        self.assertEqual(len(self.basket), 0)

    def test_getting_product_out_of_range_should_raise_error(self):
        self.assertRaises(IndexError, self.basket.get_product, 0)

    def test_total_amount_should_be_zero(self):
        self.assertEqual(self.basket.total(), 0)


class TestBasketWithOneProduct(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.basket = ShoppingBasket()
        cls.basket.add_product('milk', 3.0)

    def test_size_of_basket_should_be_one(self):
        self.assertEqual(len(self.basket), 1)

    def test_total_amount_should_have_tax(self):
        self.assertEqual(self.basket.total(), 3.63)

    def test_getting_product(self):
        self.assertEqual(self.basket.get_product(0).name, 'milk')

    def test_getting_product_out_of_range_should_raise_error(self):
        self.assertRaises(IndexError, self.basket.get_product, 1)