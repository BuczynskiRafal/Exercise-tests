import unittest


class TestJoinMethod(unittest.TestCase):

    def test_join_with_space(self):
        var1 = ' '.join(['Python', '3.8'])
        var2 = 'Python 3.8'
        self.assertEqual(var1, var2)

    def test_join_with_comma(self):
        var1 = ','.join(['open', 'high', 'low', 'close'])
        var2 = 'open,high,low,close'
        self.assertEqual(var1, var2)

    def test_join_with_new_line_char(self):
        var1 = '\n'.join(['open', 'high', 'low', 'close'])
        var2 = 'open\high\low\close'
        self.assertEqual(var1, var2)
