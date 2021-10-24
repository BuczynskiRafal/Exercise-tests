import unittest


class Doc:

    def __init__(self, string):
        self.string = string

    def __repr__(self):
        return f"Doc(string='{self.string}')"

    def __eq__(self, other):
        return len(self.string) == len(other.string)


class TestDoc(unittest.TestCase):

    def test_equal(self):
        doc3 = Doc('Technology')
        doc1 = Doc('Online')
        doc2 = Doc('Nature')
        self.assertEqual(doc1, doc2)

    def test_not_equal(self):
        doc3 = Doc('Technology')
        doc1 = Doc('Online')
        doc2 = Doc('Nature')
        self.assertNotEqual(doc3, doc1)
        self.assertNotEqual(doc3, doc2)