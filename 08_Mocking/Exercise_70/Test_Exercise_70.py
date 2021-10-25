import unittest
from Exercise_70 import *
from unittest.mock import patch


class TestGetMessage(unittest.TestCase):

    @patch('Exercise_70.get_today_name')
    def test_get_message_with_friday(self, mock_day):
        mock_day.return_value = 'Friday'
        actual = get_message()
        expect = 'Hello Friday!'
        self.assertEqual(actual, expect)


