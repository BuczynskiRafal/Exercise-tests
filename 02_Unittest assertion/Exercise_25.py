import unittest


class StringListOnly(list):

    def append(self, string):
        if not isinstance(string, str):
            raise TypeError('Only object of type str can be added to the list.')
        super().append(string)


class TestStringListOnly(unittest.TestCase):
    def test_append_string(self):
        slo = StringListOnly()
        string = 'big_data'
        slo.append(string)
        self.assertIn(string, slo)

    def test_append_not_string_should_raise_error(self):
        slo = StringListOnly()
        var1 = ['list']
        var2 = [None]
        self.assertRaises(TypeError, slo.append, var1)
        self.assertRaises(TypeError, slo.append, var2)


