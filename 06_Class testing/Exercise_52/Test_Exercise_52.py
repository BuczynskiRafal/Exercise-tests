import unittest
from Exercise_52 import Notebook


class TestNotebook(unittest.TestCase):

    def setUp(self):
        self.notebook = Notebook()
        self.notebook.new_note('Big Data')
        self.notebook.new_note('Data Science')
        self.notebook.new_note('Machine Learning')

    def test_notebook_search_method(self):
        self.assertEqual(self.notebook.search('data'), ['Big Data', 'Data Science'])