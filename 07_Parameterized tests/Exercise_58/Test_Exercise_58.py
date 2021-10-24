import unittest
from Exercise_58 import area
from Exercise_58 import perimeter


class TestArea(unittest.TestCase):

    def test_area(self):
        cases = [
            (1, 5, 5),
            (2, 10, 20),
            (100, 50, 5000)
        ]
        for width, height, result in cases:
            with self.subTest(cases=cases):
                self.assertEqual(area(width, height), result)

    def test_area_incorrect_type_should_raise_type_error(self):
        cases = [
            (1, '5'),
            ('2', 10),
            ('two', 'four')
        ]
        for width, height in cases:
            with self.subTest(cases=cases):
                self.assertRaises(TypeError, area, width, height)