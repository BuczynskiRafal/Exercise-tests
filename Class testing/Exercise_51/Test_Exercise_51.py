import unittest
from Exercise_51 import Note


class TestNote(unittest.TestCase):

    def test_note_has_category_class_attr(self):
        msg = 'Klasa Note nie posiada atrybutu category.'
        self.assertTrue(hasattr(Note, 'category'), msg=msg)
