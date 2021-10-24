import unittest


class TertLstripMethod(unittest.TestCase):
    def test_case_1(self):
        self.assertTrue(' str'.lstrip())
        self.assertFalse('str'.lstrip())


class TertStripMethod(unittest.TestCase):
    def test_case_2(self):
        self.assertTrue(' str '.strip())
        self.assertFalse('str'.strip())


class TertRstripMethod(unittest.TestCase):
    def test_case_3(self):
        self.assertTrue('str_'.rstrip())
        self.assertFalse('str'.rstrip())
