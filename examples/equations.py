from simpletex import write, save
from simpletex.document import Document, Section
from simpletex.math import (Equation,
                            Add, Subtract, Multiply, Divide)


with Document(size='11pt'):
    with Section('Inline Equations'):
        write('Example of the commutative property:')
        with Equation():
            with Multiply(symbol='times'):
                write(3)
                write(5)
            with Multiply(symbol='times'):
                write(5)
                write(3)
            write(15)
    with Section('Display Equations'):
        write('If')
        with Equation():
            write('x')
            write(5)
        write('then:')
        with Equation(inline=False):
            with Divide():
                with Add():
                    write('x')
                    write(1)
                write(3)
            with Subtract():
                write(7)
                write(5)
save('filename.tex')
