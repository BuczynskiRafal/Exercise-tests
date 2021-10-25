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
        cls.basket = ShoppingBasket().add_product('milk', 3.0)

    def test_size_of_basket_should_be_one(self):
        self.assertEqual(len(self.basket), 1)

    def test_total_amount_should_have_tax(self):
        self.assertEqual(self.basket.total(), 3.63)

    def test_getting_product(self):
        self.assertEqual('milk', self.basket.get_product(0).name)

    def test_getting_product_out_of_range_should_raise_error(self):
        self.assertRaises(IndexError, self.basket.get_product, 1)


class TestBasketWithTwoProducts(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.basket = ShoppingBasket()\
            .add_product('milk', 3.0)\
            .add_product('water', 2.0)

    def test_size_of_basket_should_be_two(self):
        self.assertEqual(len(self.basket), 2)

    def test_order_of_products(self):
        self.assertEqual((self.basket.get_product(0).name,
                          self.basket.get_product(1).name), ('milk', 'water'))

    def test_total_amount_should_have_tax(self):
        self.assertEqual(self.basket.total(), 6.05)

    def test_getting_product(self):
        self.assertEqual('milk', self.basket.get_product(0).name)

    def test_getting_product_out_of_range_should_raise_error(self):
        self.assertRaises(IndexError, self.basket.get_product, 2)
