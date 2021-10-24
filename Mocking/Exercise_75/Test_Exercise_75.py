import unittest
from unittest.mock import patch
from Exercise_75 import Programmer


class TestProgrammer(unittest.TestCase):

    def setUp(self):
        print('setting up')
        self.programmer = Programmer()
        self.programmer.add_tech('python') \
            .add_tech('sql') \
            .add_tech('java') \
            .add_tech('c++') \
            .add_tech('aws')

    @patch.object(Programmer, 'get_random_tech')
    def test_get_random_tech_mocked_python(self, mock_tech):
        mock_tech.return_value = 'python'
        actual = self.programmer.get_random_tech()
        expected = 'python'
        self.assertEqual(actual, expected)

    @patch.object(Programmer, 'get_random_tech')
    def test_get_random_tech_mocked_cpp(self, mock_tech):
        mock_tech.return_value = 'c++'
        actual = self.programmer.get_random_tech()
        expected = 'c++'
        self.assertEqual(actual, expected)