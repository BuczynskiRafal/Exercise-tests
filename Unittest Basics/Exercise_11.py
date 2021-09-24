import unittest


class TestSplitMethod(unittest.TestCase):

    def test_split_by_default(self):
        self.assertEqual('Python Testing'.split(), ['Python', 'testing'])

    def test_split_by_comma(self):
        self.assertEqual('open,high,low,close'.split(','), ['open', 'high', 'low', 'close'])

    def test_split_by_hash(self):
        self.assertEqual('summer#time#vibes'.split('#'), ['summer', 'time', 'vibes'])