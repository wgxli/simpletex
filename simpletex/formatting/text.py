"""
This module provides formatters to perform basic text formatting.

..  :copyright: (c) 2016 by Samuel Li.
    :license: GNU GPLv3, see License for more details.
"""

from simpletex.core import Formatter
from simpletex.base import Command

__all__ = ('Bold', 'Italics', 'Underline', 'SmallCaps', 'Emphasis')


class SimpleFormatter(Formatter):
    """Applies formatting to text. Generic base class."""

    def __init__(self,
                 command_name: str,
                 inline_name: str,
                 inline: bool = False):
        """
        Create a new SimpleFormatter.

        command_name : str
            The name of the default (LaTeX command)
            formatting command to use.
        inline_name : str
            The name of the inline (TeX directive)
            formatting declaration to use.
        inline : bool
            If true, the inline version of the formatter is used.
            Otherwise, use the default version.
        """
        super().__init__()
        self.command_name = command_name
        self.inline_name = inline_name
        self._inline = inline

    def _format_text(self, text) -> str:
        if self._inline:
            return '{} {}'.format(Command(self.inline_name),
                                 text)
        else:
            return Command(self.command_name, [text])


class Bold(SimpleFormatter):
    """Applies bold formatting to text."""

    def __init__(self, inline: bool = False):
        r"""
        Create a new bold formatter.

        inline : bool
            If true, the inline (``\bfshape``) version
            of the formatter is used.
            Otherwise, use the default (``\textbf{}``) version.
        """
        super().__init__('textbf', 'bfseries', inline)


class Italics(SimpleFormatter):
    """Applies italic formatting to text."""

    def __init__(self, inline: bool = False):
        r"""
        Create a new italics formatter.

        inline : bool
            If true, the inline (``\itshape``) version
            of the formatter is used.
            Otherwise, use the default (``\textit{}``) version.
        """
        super().__init__('textit', 'itshape', inline)


class Underline(SimpleFormatter):
    """Applies underline formatting to text."""

    def __init__(self):
        r"""
        Create a new underline formatter.
        
        Note that inline formatting is not supported for underlines.
        """
        super().__init__('underline', None, False)


class SmallCaps(SimpleFormatter):
    """Applies small capital formatting to text."""

    def __init__(self, inline: bool = False):
        r"""
        Create a new small capital formatter.

        inline : bool
            If true, the inline (``\scshape``) version
            of the formatter is used.
            Otherwise, use the default (``\textsc{}``) version.
        """
        super().__init__('textsc', 'scshape', inline)


class Emphasis(SimpleFormatter):
    """Applies emphasis formatting to text."""

    def __init__(self, inline: bool = False):
        r"""
        Create a new emphasis formatter.

        inline : bool
            If true, the inline (``\em``) version
            of the formatter is used.
            Otherwise, use the default (``\emph{}``) version.
        """
        super().__init__('emph', 'em', inline)
