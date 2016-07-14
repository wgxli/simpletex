import unittest
import string

from simpletex import write, clear, dump, _latex_escape
from simpletex.core import Formatter


class TestFormatter(unittest.TestCase):
    sample_text = string.printable

    def setUp(self):
        self.formatter = Formatter()
        clear()

    def test_call(self):
        self.assertEqual(self.formatter(self.sample_text),
                         self.sample_text)

    def test_call_empty(self):
        self.assertRaises(TypeError, self.formatter)

    def test_context_manager(self):
        escaped_text = _latex_escape(self.sample_text)
        with self.formatter:
            write(self.sample_text)
        self.assertEqual(dump(), escaped_text)
