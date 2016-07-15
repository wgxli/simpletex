"""
This module provides formatters to create and display LaTeX equations.

..  :copyright: (c) 2016 by Samuel Li.
    :license: GNU GPLv3, see License for more details.
"""

from simpletex.core import Formatter
from simpletex.base import Command

__all__ = ('Equation',
           'Add', 'Subtract', 'Multiply', 'Divide')


class Equation(Formatter):
    """Formats text as a LaTeX equation."""

    def __init__(self, inline: bool = True):
        r"""
        Initialize an empty equation.

        inline : bool
            Chooses the equation format to use.
            If ``True``, use the inline (``$``) syntax.
            If ``False``, use the display-style (``$$``) syntax.
        """
        self._symbol = '$' if inline else '$$'

    def _format_text(self, text) -> str:
        """
        Format the given text as a LaTeX equation.

        text : iterable of str
            The text of the equation.
            The elements in the text are joined by equals signs,
            and then formatted as a LaTeX equation.
        """
        return "{}{}{}".format(self._symbol,
                               ' = '.join(map(str, text)),
                               self._symbol)


class Operator(Formatter):
    """A generic base class for arbitrary mathematical operators."""

    def __init__(self, operator: str):
        """Initialize an operation with the given operator symbol."""
        super().__init__()
        self._operator = str(operator)

    def _format_text(self, text) -> str:
        """
        Format the given text using the generic operation.

        text : iterable of str
            The elements in the given text will be conveted to strings
            and then joined by the operator symbol.
        """
        return self._operator.join(map(str, text))


class Add(Operator):
    """Adds arguments together in symbolic form."""

    def __init__(self):
        """Initialize an empty addition operator."""
        super().__init__('+')


class Subtract(Operator):
    """Subtracts two given arguments in symbolic form."""

    def __init__(self, inline: bool = False):
        """Initialize an empty subtraction operator."""
        super().__init__('-')


class Multiply(Operator):
    """Multiplies arguments together in symbolic form."""

    _SYMBOL_DICT = {None: '',
                    'dot': Command('cdot '),
                    'cross': Command('times '),
                    'times': Command('times ')}
    """
    An internal dictionary storing the symbols' names
    and their corresponding TeX commands.
    """

    def __init__(self, symbol='dot'):
        r"""
        Initialize an empty multiplication operator.

        symbol : str or None
            Chooses the multiplication symbol to use.
            If ``None``, no explicit symbol is used.
            If 'dot', a dot-style (``\cdot``) operator is used.
            If 'cross' or 'times', a cross-style (``\times``) operator is used.
        """
        super().__init__(self._SYMBOL_DICT[symbol])


class Divide(Operator):
    """Divides two given arguments in symbolic form."""

    def __init__(self, inline: bool = False):
        r"""
        Initialize an empty division operator.

        inline : bool
            Chooses division format to use.
            If ``False``, use the display-style (``\frac{}{}``) syntax.
            If ``True``, use the inline (``/``) syntax.
        """
        # We will override the text formatting, initialize with dummy symbol
        super().__init__('')
        self._inline = inline

    def _format_text(self, text) -> str:
        """
        Format the given text using the division operator.

        text : iterable of str
            Must have a length of two. The first element is the numerator,
            and the second is the denominator.
            If the length is not two, throws a ``ValueError``.
        """
        if len(text) != 2:
            error_string = '{} operation must have exactly two arguments.'
            raise ValueError(error_string.format(self.__class__.__name__))
        else:
            if self._inline:
                return '{}/{}'.format(*text)
            else:
                return Command('frac', text)
