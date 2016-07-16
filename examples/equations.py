from simpletex import write, save
from simpletex.document import Document, Section
from simpletex.math import (Equation,
                            Add, Subtract, Multiply, Divide)


with Document(size='11pt'):
    with Section('Inline Equations'):
        write('Example of the commutative property:')
        with Equation():
            with Multiply(symbol='x'):
                write(3)
                write(5)
            write(Multiply(symbol='times')(5, 3))
            write(15)
    with Section('Display Equations'):
        write('If')
        with Equation():
            write('x')
            write(5)
        write('then:')
        with Equation(inline=False):
            with Divide():
                write(Add()('x', 1))
                write(3)
            write(Subtract()(7, 5))
save('filename.tex')
