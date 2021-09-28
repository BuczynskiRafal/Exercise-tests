import unittest
from Exercise_57 import area
from Exercise_57 import perimeter


class TestArea(unittest.TestCase):

    def test_area(self):
        cases =[
            (1, 5, 5),
            (2, 10, 20),
            (100, 50, 5000)
        ]
        for width, height, result in cases:
            with self.subTest(cases=cases):
                self.assertEqual(area(width, height), result)
                # self.assertEqual(perimeter(width, height), result)