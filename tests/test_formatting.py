import unittest
import string

from simpletex.formatting.text import Bold, Italics, Underline


SAMPLE_TEXT = 'simpletex'

class TestBold(unittest.TestCase):
    def test_inline(self):
        self.assertEqual(Bold(inline=True)(SAMPLE_TEXT),
                '\\bfseries ' + SAMPLE_TEXT)
    
    def test_command(self):
        self.assertEqual(str(Bold(inline=False)(SAMPLE_TEXT)),
                '\\textbf{' + SAMPLE_TEXT + '}')

    def test_default(self):
        self.assertEqual(str(Bold()(SAMPLE_TEXT)),
                '\\textbf{' + SAMPLE_TEXT + '}')


class TestItalics(unittest.TestCase):
    def test_inline(self):
        self.assertEqual(Italics(inline=True)(SAMPLE_TEXT),
                '\\itshape ' + SAMPLE_TEXT)
    
    def test_command(self):
        self.assertEqual(str(Italics(inline=False)(SAMPLE_TEXT)),
                '\\textit{' + SAMPLE_TEXT + '}')

    def test_default(self):
        self.assertEqual(str(Italics()(SAMPLE_TEXT)),
                '\\textit{' + SAMPLE_TEXT + '}')


class TestUnderline(unittest.TestCase):
    def test_default(self):
        self.assertEqual(str(Underline()(SAMPLE_TEXT)),
                '\\underline{' + SAMPLE_TEXT + '}')
