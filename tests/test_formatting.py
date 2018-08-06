import unittest
import string

from simpletex import write, dump, clear
from simpletex.formatting.text import Bold, Italics, Underline
from simpletex.formatting.layout import Centering, Columns


SAMPLE_TEXT = 'simpletex'

class TestBold(unittest.TestCase):
    def test_inline(self):
        self.assertEqual(Bold(inline=True)(SAMPLE_TEXT),
                '\\bfseries ' + SAMPLE_TEXT)
    
    def test_command(self):
        self.assertEqual(str(Bold(inline=False)(SAMPLE_TEXT)),
                '\\textbf{' + SAMPLE_TEXT + '}')

    def text_context_manager(self):
        with Bold():
            write(SAMPLE_TEXT)
        self.assertEqual(dump(), '\\textbf{' + SAMPLE_TEXT + '}')
        clear()

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

    def text_context_manager(self):
        with Italics():
            write(SAMPLE_TEXT)
        self.assertEqual(dump(), '\\textit{' + SAMPLE_TEXT + '}')
        clear()

    def test_default(self):
        self.assertEqual(str(Italics()(SAMPLE_TEXT)),
                '\\textit{' + SAMPLE_TEXT + '}')


class TestUnderline(unittest.TestCase):
    def test_default(self):
        self.assertEqual(str(Underline()(SAMPLE_TEXT)),
                '\\underline{' + SAMPLE_TEXT + '}')

    def text_context_manager(self):
        with Underline():
            write(SAMPLE_TEXT)
        self.assertEqual(dump(), '\\underline{' + SAMPLE_TEXT + '}')
        clear()


class TestCentering(unittest.TestCase):
    def test_inline(self):
        self.assertEqual(str(Centering(inline=True)(SAMPLE_TEXT)),
                '\\centering ' + SAMPLE_TEXT)

    def test_command(self):
        self.assertEqual(str(Centering()(SAMPLE_TEXT)), '\n'.join([
            r'\begin{center}',
            '\t' + SAMPLE_TEXT,
            r'\end{center}'
        ]))

    def test_context_manager(self):
        with Centering():
            write(SAMPLE_TEXT)
        self.assertEqual(dump(), '\n'.join([
            r'\begin{center}',
            '\t' + SAMPLE_TEXT,
            r'\end{center}'
        ]))
        clear()

    def test_inline_context_manager(self):
        with Centering(inline=True):
            write(SAMPLE_TEXT)
        self.assertEqual(dump(),
                '\\centering ' + SAMPLE_TEXT)
        clear()


class TestColumns(unittest.TestCase):
    def test_command(self):
        self.assertEqual(str(Columns()(SAMPLE_TEXT)), '\n'.join([
            r'\begin{multicols}',
            '\t' + SAMPLE_TEXT,
            r'\end{multicols}'
        ]))

    def test_context_manager(self):
        with Columns(3):
            write(SAMPLE_TEXT)
        self.assertEqual(dump(), '\n'.join([
            r'\usepackage{multicol}',
            '',
            r'\begin{multicols}{3}',
            '\t' + SAMPLE_TEXT,
            r'\end{multicols}'
        ]))
        clear()
