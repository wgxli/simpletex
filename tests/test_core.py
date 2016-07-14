import unittest
import string

from simpletex import write, clear, dump, _latex_escape
from simpletex.core import Formatter, Text, Paragraph, Registry

SAMPLE_TEXT = string.printable


class TestFormatter(unittest.TestCase):
    def setUp(self):
        self.formatter = Formatter()
        clear()

    def test_call(self):
        self.assertEqual(self.formatter(SAMPLE_TEXT),
                         SAMPLE_TEXT)

    def test_call_empty(self):
        self.assertRaises(TypeError, self.formatter)

    def test_context_manager(self):
        escaped_text = _latex_escape(SAMPLE_TEXT)
        with self.formatter:
            write(SAMPLE_TEXT)
        self.assertEqual(dump(), escaped_text)


class TestText(unittest.TestCase):
    def setUp(self):
        self.text = Text()

    def write_attribute(self):
        self.text.new_attribute = SAMPLE_TEXT

    def write_multiple_attributes(self):
        self.text.a = 'X'
        self.text.b = 'Y'

    def test_get_missing(self):
        self.assertEqual(self.text.missing_attribute, '')

    def test_set_missing(self):
        self.write_attribute()
        self.assertEqual(self.text.new_attribute, SAMPLE_TEXT)

    def test_set_exists(self):
        self.text.new_attribute = 5
        self.write_attribute()
        self.assertEqual(self.text.new_attribute, SAMPLE_TEXT)
        self.text.new_attribute = 12
        self.assertEqual(self.text.new_attribute, 12)

    def test_contains_missing(self):
        self.assertFalse('missing_attribute' in self.text)

    def test_contains_exists(self):
        self.write_attribute()
        self.assertTrue('new_attribute' in self.text)

    def test_iter_empty(self):
        self.assertEqual(list(self.text), [])

    def test_iter_nonempty(self):
        self.write_multiple_attributes()
        self.assertEqual(list(self.text), ['X', 'Y'])

    def test_repr_empty(self):
        self.assertEqual(repr(self.text), 'Text[]')

    def test_repr_nonempty(self):
        self.write_multiple_attributes()
        self.assertEqual(repr(self.text), "Text['a', 'b']")

    def test_str_empty(self):
        self.assertEqual(str(self.text), '')

    def test_str_nonempty(self):
        self.write_multiple_attributes()
        self.assertEqual(str(self.text), "XY")

    def test_context_manager(self):
        self.assertRaises(TypeError, self.text.__enter__)
        self.assertEqual(self.text.__exit__(), None)


class TestParagraph(unittest.TestCase):
    def setUp(self):
        self.par = Paragraph()

    def write_lines(self):
        self.par.write('A')
        self.par.write('B')

    def test_len_empty(self):
        self.assertEqual(len(self.par), 0)

    def test_len_nonempty(self):
        self.write_lines()
        self.assertEqual(len(self.par), 2)

    def test_iter_empty(self):
        self.assertEqual(list(self.par), [])

    def test_iter_nonempty(self):
        self.write_lines()
        self.assertEqual(list(self.par), ['A', 'B'])

    def test_str_empty(self):
        self.assertEqual(str(self.par), '')

    def test_str_nonempty(self):
        self.write_lines()
        self.assertEqual(str(self.par), 'A\nB')

    def test_context_manager(self):
        self.assertRaises(TypeError, self.par.__enter__)
        self.assertEqual(self.par.__exit__(), None)

class TestRegistry(unittest.TestCase):
    COMPLEX_OBJECT = {'A': ['B', ('C', 'D')], 'E':None, False:'F'}
    
    def setUp(self):
        self.reg = Registry()

    def register_entries(self):
        self.reg.register('A')
        self.reg.register('B', self.COMPLEX_OBJECT)

    def test_len_empty(self):
        self.assertEqual(len(self.reg), 0)

    def test_len_nonempty(self):
        self.register_entries()
        self.assertEqual(len(self.reg), 2)

    def test_iter_empty(self):
        self.assertEqual(list(self.reg), [])

    def test_iter_nonempty(self):
        self.register_entries()
        self.assertEqual(list(self.reg), ['A', 'B'])

    def test_contains_missing(self):
        self.assertFalse('missing_key' in self.reg)

    def test_contains_exists(self):
        self.register_entries()
        self.assertTrue('A' in self.reg)
        self.assertTrue('B' in self.reg)

    def test_items_empty(self):
        self.assertEqual(list(self.reg.items()), [])

    def test_items_nonempty(self):
        self.register_entries()
        self.assertEqual(list(self.reg.items()), [('A', None),
                                                 ('B', self.COMPLEX_OBJECT)])

    def test_str_empty(self):
        self.assertEqual(str(self.reg), '')

    def test_str_nonempty(self):
        self.register_entries()
        self.assertEqual(str(self.reg), 'A\nB')
