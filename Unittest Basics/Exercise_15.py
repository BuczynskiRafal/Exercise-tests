import unittest


class TestUpper(unittest.TestCase):

    def test_upper(self):
        self().assertEqual('summer'.upper(), 'SUMMER')

    def test_is_upper(self):
        self.assertEqual('SUMMER'.isupper(), True)
        self.assertEqual('summer'.isupper(), False)