import unittest

from simpletex.base import Brace, Command, Environment


class TestBrace(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(Brace()(), '')

    def test_args(self):
        self.assertEqual(Brace()('a', 'b', 'c'), '{a}{b}{c}')


class TestCommand(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(str(Command('a')), r'\a')

    def test_arguments(self):
        self.assertEqual(str(Command('a',
                                     ['b', 'c'])), r'\a{b}{c}')

    def test_options(self):
        self.assertEqual(str(Command('a',
                                     [],
                                     'b', 'c')), r'\a[b, c]')

    def test_kwoptions(self):
        self.assertIn(str(Command('a',
                                  [],
                                  d='e',
                                  b='c')),
                      (r'\a[b=c, d=e]',
                       r'\a[d=e, b=c]'))

    def test_all(self):
        self.assertIn(str(Command('a',
                                  ['b', 'c'],
                                  'd', 'e',
                                  f='g', h='i')),
                         (r'\a[d, e, f=g, h=i]{b}{c}',
                          r'\a[d, e, h=i, f=g]{b}{c}'))


class TestEnvironment(unittest.TestCase):
    def test_no_name(self):
        self.assertRaises(ValueError, Environment(), '')

    def test_empty(self):
        self.assertEqual(Environment('name')(''),
                         '\\begin{name}\n\n\\end{name}')

    def test_single_line(self):
        self.assertEqual(Environment('name')('text'),
                         '\\begin{name}\n\ttext\n\\end{name}')

    def test_multiline(self):
        self.assertEqual(Environment('name')('a\nb'),
                         '\\begin{name}\n\ta\n\tb\n\\end{name}')
