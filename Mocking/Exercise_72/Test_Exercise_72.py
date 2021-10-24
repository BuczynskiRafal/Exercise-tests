import unittest
from unittest.mock import patch
from Exercise_72 import get_code_with_day
from Exercise_72 import get_today_name

class TestGetCodeWithDay(unittest.TestCase):

    @patch('Exercise_72.get_today_name')
    @patch('random.randint')
    def test_get_code_with_day_with_mocked_friday(self, mock_rand, mock_friday):
        mock_friday.return_value = 'FRI'
        mock_rand.return_value = 30
        actual = get_code_with_day()
        expected = 'CX-30-FRI'
        self.assertEqual(expected, actual)
