import unittest
from Exercise_79 import Product


class TestProduct( unittest.TestCase ):

    def setUp(self):
        self.product = Product( 'milk', 3.0 )

    def test_get_product_name(self):
        self.assertEqual( self.product.name, 'milk' )

    def test_get_product_price(self):
        self.assertEqual( self.product.price, 3.0 )

    def test_get_quantity(self):
        self.assertEqual( self.product.quantity, 1 )

    def test_repr_method(self):
        self.assertEqual(self.product.__repr__(), f"Product(name='milk', price=3.0, quantity=1)")