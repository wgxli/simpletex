"""
This module provides formatters to create sequences and lists.

..  :copyright: (c) 2016 by Samuel Li.
    :license: GNU GPLv3, see License for more details.
"""

from simpletex.core import Formatter
from simpletex.base import Environment

__all__ = ('OrderedList', 'UnorderedList', 'Description')


class ItemList(Formatter):
    """Formats a given list of text as a LaTeX item list."""

    @staticmethod
    def _format_text(text) -> str:
        """
        Format the given text into a LaTeX item list.

        text : iterable of pairs, mapping, or iterable of items
            If pairs or a mapping are given, the first component of each entry
            will be used as the item key, and the second as the value.
            Otherwise, do not use a key in the item command.
        """
        try:
            return '\n'.join(r'\item[{}] {}'.format(key, item)
                             for key, item in text.items())
        except AttributeError:
            try:
                return '\n'.join(r'\item[{}] {}'.format(key, item)
                                 for key, item in text)
            except ValueError:
                return '\n'.join(r'\item {}'.format(item) for item in text)


class OrderedList(Environment):
    """
    Formats a given list of text as a numbered LaTeX list.

    Equivalent to the LaTeX ``enumerate`` environment.
    """

    def __init__(self):
        """Create an empty numbered list."""
        super().__init__('enumerate')

    def _format_text(self, text) -> str:
        r"""Format a single item in the list into an ``\item`` entry."""
        return super()._format_text(ItemList()(text))


class UnorderedList(Environment):
    """
    Formats a given list of text as a bulleted LaTeX list.

    Equivalent to the LaTeX ``itemize`` environment.
    """

    bullet = None
    """
    The bullet to be used for each item entry.

    If ``None``, no bullet is used.
    """

    def __init__(self):
        """Create an empty bulleted list."""
        super().__init__('itemize')

    def _format_text(self, text) -> str:
        r"""Format a single item in the list into an ``\item`` entry."""
        if self.bullet is None:
            return super()._format_text(ItemList()(text))
        else:
            list_item_pairs = [(self.bullet, item) for item in text]
            return super()._format_text(ItemList()(list_item_pairs))


class Description(Environment):
    """
    Formats a given list of key-value pairs as a LaTeX description list.

    Equivalent to the LaTeX ``description`` environment.
    """

    def __init__(self):
        """Create an empty description list."""
        super().__init__('description')

    def _format_text(self, text) -> str:
        """Format a single key-value pair in the list as LaTeX."""
        return super()._format_text(ItemList()(text))
