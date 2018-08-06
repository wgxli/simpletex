import unittest
import string

from simpletex import write, clear, dump, save
from simpletex.document import Document, Section, Subsection


SAMPLE_TEXT = 'simpletex'
SAMPLE_HEADING = 'Heading Text'

HEADER = '\n'.join([r'\documentclass[12pt]{article}', '', r'\usepackage[utf8]{inputenc}', '', r'\begin{document}'])
FOOTER = r'\end{document}'
         

class TestDocument(unittest.TestCase):
    def test_document(self):
        with Document():
            write(SAMPLE_TEXT)
        expected_string = '\n'.join([
            HEADER,
            '\t' + SAMPLE_TEXT,
            FOOTER
        ])
        self.assertEqual(dump(),
                expected_string)
        clear()

    def tearDown(self):
        clear()


class TestSection(unittest.TestCase):
    def test_section(self):
        with Document():
            with Section(SAMPLE_HEADING):
                write(SAMPLE_TEXT)
        expected_string = '\n'.join([
            HEADER,
            '\t\\section{' + SAMPLE_HEADING + '}',
            '\t\t' + SAMPLE_TEXT,
            FOOTER
        ])
        self.assertEqual(dump(),
                expected_string)
        clear()

    def tearDown(self):
        clear()


class TestSubsection(unittest.TestCase):
    def test_subsection(self):
        with Document():
            with Subsection(SAMPLE_HEADING):
                write(SAMPLE_TEXT)
        expected_string = '\n'.join([
            HEADER,
            '\t\\subsection{' + SAMPLE_HEADING + '}',
            '\t\t' + SAMPLE_TEXT,
            FOOTER
        ])
        self.assertEqual(dump(),
                expected_string)
        clear()

    def tearDown(self):
        clear()


