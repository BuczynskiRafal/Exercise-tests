import unittest
from unittest.mock import patch
from Exercise_69 import get_code


class TestGetCode(unittest.TestCase):

    @patch('random.randint')
    def test_get_code_mock_should_return_30(self, mock_random):
        mock_random.return_value = '30'
        actual = get_code()
        expect = 'CX-30'
        self.assertEqual(actual, expect)
