"""
Text Formatting
===============
This module provides utilities to perform basic text formatting.

..  :copyright: (c) 2016 by Samuel Li.
    :license: GNU GPLv3, see License for more details.
"""

from simpletex.core import Formatter
from simpletex.base import Command, Environment

__all__ = ['Bold', 'Italics', 'Underline', 'SmallCaps', 'Emphasis']

class SimpleFormatter(Formatter):
    """Applies formatting to text. Generic base class."""
    def __init__(self, command_name, inline_name, inline=False):
        """
        command_name : str
            The name of the LaTeX formatting command to use.
        inline_name : str
            The name of the inline formatting declaration to use.
        inline : bool
            If true, the inline LaTeX declaration is used instead
            of the command form.
        """
        super().__init__()
        self.command_name = command_name
        self.inline_name = inline_name
        self._inline = inline

    def _format_text(self, text: str) -> str:
        if self._inline:
            return '{}{}'.format(Command(self.inline_name),
                                 text)
        else:
            return Command(self.command_name, [text])


class Bold(SimpleFormatter):
    """Applies bold formatting to text."""
    def __init__(self, inline=False):
        super().__init__('textbf', 'bfshape', inline)


class Italics(SimpleFormatter):
    """Applies italic formatting to text."""
    def __init__(self, inline=False):
        super().__init__('textit', 'itshape', inline)


class Underline(SimpleFormatter):
    """Applies underline formatting to text."""
    def __init__(self, inline=False):
        super().__init__('underline', 'underline', inline)


class SmallCaps(SimpleFormatter):
    """Applies small capital formatting to text."""
    def __init__(self, inline=False):
        super().__init__('textsc', 'scshape', inline)


class Emphasis(SimpleFormatter):
    """Applies emphasis formatting to text."""
    def __init__(self, inline=False):
        super().__init__('emph', 'em', inline)
