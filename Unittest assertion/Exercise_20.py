import unittest


def calculate_daily_return(open, close):
    return round((close / open - 1) * 100, )


class TestCalculateDailyReturn(unittest.TestCase):

    def test_positive_return(self):
        self.assertAlmostEqual(calculate_daily_return(349, 360), 3.15)

    def test_negative_return(self):
        self.assertAlmostEqual(calculate_daily_return(349, 340), -2.58)

    def test_zero_return(self):
        self.assertAlmostEqual(calculate_daily_return(349, 349), 0.0)