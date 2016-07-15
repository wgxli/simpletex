"""
This module provides utilities to combine multiple formatters.

..  :copyright: (c) 2016 by Samuel Li.
    :license: GNU GPLv3, see License for more details.
"""

from simpletex.core import Formatter

__all__ = ('Style',)


class Style(Formatter):
    """
    Allows combining multiple formatters into a single formatter.

    Formatter instances can be applied to a ``Style``.
    The ``Style`` will then format any given text by applying each
    formatter in the order given.
    """

    def __init__(self, inline: bool = False):
        """
        Create a new, empty style.

        By default, applies no formatting to text.

        inline : bool
            If true, the inline (TeX directive) version of each
            applied formatter is used. Otherwise, use the default
            (LaTeX command) version of each formatter.
        """
        super().__init__()
        self._formatters = []
        self._inline = inline

    def apply(self, formatter: Formatter):
        """
        Apply the given formatter to the style.

        Applied formatters are stored in the style, and
        are used in the order applied when formatting text.

        formatter : Formatter
            The formatter to apply.
            Must be an instance of ``Formatter`` or a subclass.
        """
        if not isinstance(formatter, Formatter):
            error_string = '{} is not a Formatter.'
            raise TypeError(error_string.format(formatter.__class__.__name__))
        formatter._inline = self._inline
        self._formatters.append(formatter)

    def _format_text(self, text) -> str:
        """
        Apply formatting to the given text.

        Each stored formatter is applied to the text in succesion,
        in the order they were stored.

        text : str-like
            The text to be formatted.
        """
        for formatter in self._formatters:
            text = formatter(text)
        return text

    def __bool__(self):
        """Return ``False`` if no formatters applied, else ``True``."""
        return bool(self._formatters)

    def __repr__(self):
        """Display the class name and the currently applied formatters."""
        return '{}{}'.format(self.__class__.__name__, self._formatters)
