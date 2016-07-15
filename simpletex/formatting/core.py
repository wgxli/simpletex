"""
This module provides useful low-level formatting utilities.

..  :copyright: (c) 2016 by Samuel Li.
    :license: GNU GPLv3, see License for more details.
"""

from simpletex.core import Formatter

__all__ = ('Indent',)


class Indent(Formatter):
    """Indents the given text by one level."""

    def _format_text(self, text) -> str:
        """
        Indent the given text by one level.

        The text is split by line feed characters,
        and each line is then indented individually.
        """
        lines = str(text).split('\n')
        return '\n'.join(map(self._tab_line, lines))

    @staticmethod
    def _tab_line(text: str) -> str:
        if text != '':
            text = '\t' + text
        return text
