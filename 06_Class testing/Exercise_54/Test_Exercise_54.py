import unittest
from Exercise_54 import Product


class TestProduct(unittest.TestCase):

    def test_product_has_get_id_function_attribute(self):
        self.assertTrue(hasattr(Product, 'get_id'))
        self.assertTrue(callable(Product.get_id))