import unittest
from unittest.mock import patch
from Exercise_71 import get_message


class TestGetMessage(unittest.TestCase):

    @patch('Exercise_71.get_today_name')
    def test_get_message_with_friday(self, mock_day):
        mock_day.return_value = 'Friday'
        actual = get_message()
        expected = 'Hello Friday!'
        self.assertEqual(actual, expected)

    @patch('Exercise_71.get_today_name')
    def test_get_message_with_monday(self, mock_day):
        mock_day.return_value = 'Monday'
        actual = get_message()
        excepted = 'Hello Monday!'
        self.assertEqual(actual, excepted)
