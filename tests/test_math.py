import unittest
import numpy as np

from simpletex import write, clear, dump
from simpletex.math import (Equation,
                            Add, Subtract, Multiply, Divide,
                            Matrix)

DATA = [[1, 2], [3, 4]]
NP_DATA = np.array(DATA)
MAT_ENV = '\\begin{{Bmatrix}}\n{}\n\\end{{Bmatrix}}'


class TestEquation(unittest.TestCase):
    def setUp(self):
        clear()

    def test_inline_empty(self):
        self.assertEqual(str(Equation()('')), '$$')

    def test_display_empty(self):
        self.assertEqual(str(Equation(inline=False)('')),
                         '$$$$')

    def test_inline(self):
        with Equation():
            write('x')
            write(5)
            write(17)
        self.assertEqual(dump(), '$x = 5 = 17$')

    def test_display(self):
        with Equation(inline=False):
            write('x')
            write(5)
            write(17)
        self.assertEqual(dump(), '$$x = 5 = 17$$')

    def tearDown(self):
        clear()


class TestAdd(unittest.TestCase):
    def setUp(self):
        self.add = Add()
        clear()

    def test_call_empty(self):
        self.assertEqual(str(self.add('')), '')

    def test_write_empty(self):
        with self.add:
            pass
        self.assertEqual(dump(), '')

    def test_call(self):
        self.assertEqual(str(self.add(3, 5, 7)), '3+5+7')

    def test_write(self):
        with self.add:
            write(3)
            write(5)
            write(7)
        self.assertEqual(dump(), '3+5+7')

    def tearDown(self):
        clear()


class TestSubtract(unittest.TestCase):
    def setUp(self):
        self.sub = Subtract()
        clear()

    def test_call_empty(self):
        self.assertEqual(str(self.sub('')), '')

    def test_write_empty(self):
        with self.sub:
            pass
        self.assertEqual(dump(), '')

    def test_call(self):
        self.assertEqual(str(self.sub(3, 5)), '3-5')

    def test_write(self):
        with self.sub:
            write(3)
            write(5)
        self.assertEqual(dump(), '3-5')

    def tearDown(self):
        clear()


class TestMultiply(unittest.TestCase):
    def setUp(self):
        self.mul = Multiply(symbol='*')
        clear()

    def test_call_empty(self):
        self.assertEqual(str(self.mul('')), '')

    def test_write_empty(self):
        with self.mul:
            pass
        self.assertEqual(dump(), '')

    def test_call(self):
        self.assertEqual(str(self.mul(3, 5, 7)), '3*5*7')

    def test_write(self):
        with self.mul:
            write(3)
            write(5)
            write(7)
        self.assertEqual(dump(), '3*5*7')

    def tearDown(self):
        clear()


class TestDivide(unittest.TestCase):
    def setUp(self):
        clear()

    def test_call_display(self):
        div = Divide()
        self.assertEqual(str(div(3, 5)), r'\frac{3}{5}')

    def test_call_inline(self):
        div = Divide(inline=True)
        self.assertEqual(str(div(3, 5)), r'3/5')

    def test_write_display(self):
        with Divide():
            write(3)
            write(5)
        self.assertEqual(dump(), r'\frac{3}{5}')

    def test_write_inline(self):
        with Divide(inline=True):
            write(3)
            write(5)
        self.assertEqual(dump(), r'3/5')

    def test_error_invalid(self):
        self.assertRaises(ValueError, Divide(), 3)

    def test_error_short(self):
        self.assertRaises(ValueError, Divide(), [3])

    def test_error_long(self):
        self.assertRaises(ValueError, Divide(), [3, 1, 4])

    def tearDown(self):
        clear()


class TestMatrix(unittest.TestCase):
    def setUp(self):
        self.mat = Matrix(brackets='{')
        clear()

    def test_empty(self):
        self.assertEqual(str(self.mat('')), MAT_ENV.format(''))

    def test_call_no_numpy(self):
        self.assertEqual(self.mat(DATA),
                         MAT_ENV.format('\t1 & 2 \\\\\n\t3 & 4 \\\\'))

    def test_call_numpy(self):
        self.assertEqual(self.mat(NP_DATA),
                         MAT_ENV.format('\t1 & 2 \\\\\n\t3 & 4 \\\\'))

    def test_write(self):
        with self.mat:
            for line in DATA:
                write(line)
        self.assertEqual(dump(),
                         MAT_ENV.format('\t1 & 2 \\\\\n\t3 & 4 \\\\'))

    def tearDown(self):
        clear()

