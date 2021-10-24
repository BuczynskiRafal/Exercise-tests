import unittest


class Container:
    pass


class TestContainer(unittest.TestCase):

    def test_container(self):
        self.assertIsInstance(Container, type)

    @unittest.skip('The Container class requires implementation.')
    def test_has_code_attribute(self):
        msg = 'The Container class does not have a code attribute.'
        self.assertTrue(hasattr(Container, 'code'), msg)


if __name__ == '__main__':
    unittest.main()