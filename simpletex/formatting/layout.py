"""
This module provides formatters to control document and text layout.

..  :copyright: (c) 2016 by Samuel Li.
    :license: GNU GPLv3, see License for more details.
"""

from simpletex import usepackage
from simpletex.base import Command, Environment

__all__ = ('Centering', 'Columns')


class Centering(Environment):
    """
    Centers all contents.

    Equivalent to the LaTeX ``center`` environment.
    """

    def __init__(self, inline: bool = False):
        r"""
        Create a new centering formatter.

        inline : bool
            If true, the inline (``\centering``) version
            of the formatter is used.
            Otherwise, use the default (``\begin{center}``) version.
        """
        super().__init__('center')
        self._inline = inline

    def _format_text(self, text) -> str:
        if self._inline:
            return '{} {}'.format(Command('centering'), text)
        else:
            return super()._format_text(text)


class Columns(Environment):
    """
    Formats contents into columns.

    Equivalent to the LaTeX ``multicols`` environment.
    """

    def __init__(self, number: int = 2):
        """
        Create a new ``multicols`` environment.

        Automatically imports the required ``multicol`` package.

        number : int
            The number of columns to use.
        """
        if number == 2:
            super().__init__('multicols')
        else:
            super().__init__('multicols', number)
        usepackage('multicol')
