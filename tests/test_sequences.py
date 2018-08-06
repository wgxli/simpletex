import unittest
import string

from simpletex import write, dump, clear
from simpletex.sequences import OrderedList, UnorderedList, Description


SAMPLE_ITEMS = ['simpletex', 'latex', 'python']
SAMPLE_MAPPING = {'monty': 'python', 'marco': 'polo'}

FORMATTED_ITEMS = '\n'.join('\t\\item ' + item for item in SAMPLE_ITEMS)
FORMATTED_MAPPING = '\n'.join('\t\\item[' + key + '] ' + value for key, value in SAMPLE_MAPPING.items())

class TestOrderedList(unittest.TestCase):
    def setUp(self):
        self.expectedString = '\n'.join([
            r'\begin{enumerate}',
            FORMATTED_ITEMS,
            r'\end{enumerate}'
        ])

    def test_inline(self):
        self.assertEqual(OrderedList()(SAMPLE_ITEMS), self.expectedString)

    def test_context_manager(self):
        with OrderedList():
            [write(item) for item in SAMPLE_ITEMS]
        self.assertEqual(dump(), self.expectedString)
        clear()

    def tearDown(self):
        clear()


class TestUnorderedList(unittest.TestCase):
    def setUp(self):
        self.expectedString = '\n'.join([
            r'\begin{itemize}',
            FORMATTED_ITEMS,
            r'\end{itemize}'
        ])

    def test_inline(self):
        self.assertEqual(UnorderedList()(SAMPLE_ITEMS), self.expectedString)

    def test_context_manager(self):
        with UnorderedList():
            [write(item) for item in SAMPLE_ITEMS]
        self.assertEqual(dump(), self.expectedString)
        clear()

    def tearDown(self):
        clear()


class TestDescription(unittest.TestCase):
    def setUp(self):
        self.expectedString = '\n'.join([
            r'\begin{description}',
            FORMATTED_MAPPING,
            r'\end{description}'
        ])

    def test_inline(self):
        self.assertEqual(Description()(SAMPLE_MAPPING), self.expectedString)

    def test_context_manager(self):
        with Description():
            [write(key, value) for key, value in SAMPLE_MAPPING.items()]
        self.assertEqual(dump(), self.expectedString)
        clear()

    def tearDown(self):
        clear()
