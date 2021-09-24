import os
import sys
import unittest


class Container:

    def __init__(self):
        if sys.platform.startswith('win'):
            self.code = 'XC-win'
        else:
            self.code = f'XC-{sys.platform}'


class TestContainer(unittest.TestCase):

    @unittest.skipUnless(sys.platform.startswith('win'), 'Requires windows')
    def test_requires_windows(self):
        c = Container()
        self.assertEqual(c.code, 'XC-win')

    @unittest.skipUnless(sys.platform.startswith('lin'), 'Requires linux')
    def test_requires_linux(self):
        c = Container()
        self.assertEqual(c.code, 'XC-linux')