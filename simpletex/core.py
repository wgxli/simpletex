"""
This module provides base classes forming the core of simpletex.

..  :copyright: (c) 2016 by Samuel Li.
    :license: GNU GPLv3, see License for more details.
"""

from collections import defaultdict, OrderedDict

import simpletex


class Formatter:
    """
    Formats text in an arbitrary style.

    Can be either called or used as a context manager.
    When called, formats the arguments.
    When used as a context manager, all text written within
    the context manager is passed to the formatter upon exit.
    """

    def __call__(self, *args, **kwargs) -> str:
        """Format the given arguments into a string."""
        if not args and not kwargs:
            error_string = "Can't re-instantiate an instance of {}."
            raise TypeError(error_string.format(self.__class__.__name__))
        else:
            return self._format_text(*args, **kwargs)

    # Should be overridden by subclasses
    @staticmethod
    def _format_text(text) -> str:
        return str(text)

    def __enter__(self):
        """Add self to the global context stack."""
        simpletex._CONTEXT.push(Paragraph())

    def __exit__(self, *args):
        """
        Format any written text, writing it to the global context stack.

        First removes self from the context stack.
        Formats any text written within the context manager,
        and writes it to the object at the top of the
        context stack.
        """
        formatted_text = self(simpletex._CONTEXT.pop())
        simpletex._CONTEXT.write(formatted_text)


class Text:
    """
    Acts as a body of text, with each line named and addressable.

    Bodies of text are read by reading any attribute,
    and created by setting any attribute.
    Reading a non-existent attribute will automatically create
    a blank line of text.
    """

    def __init__(self):
        """Initialize the text body."""
        super().__setattr__('_text', defaultdict(lambda: ''))
        super().__setattr__('_order', [])

    def __getattr__(self, name: str):
        """
        Return the line of text with the given name.

        If the specified line name was already set, return stored value.
        Otherwise, create a blank line with the given name,
        returning an empty string.
        """
        if name not in self:
            self._order.append(name)
        return self._text[name]

    def __setattr__(self, name, value):
        """Write a line of text under the given name."""
        if name not in self:
            self._order.append(name)
        self._text[name] = value

    def __contains__(self, item):
        """Determine if a given line name exists in the text body."""
        return item in self._order

    def __iter__(self):
        """Iterate over the text in the text body."""
        return (self._text[line] for line in self._order)

    def __repr__(self):
        """Show the instance's class name and the names of its text lines."""
        return "{}{}".format(self.__class__.__name__, self._order)

    def __str__(self):
        """Should be overridden by subclasses."""
        return ''.join(map(str, self))

    def __enter__(self):
        """Raise an error; cannot be used as a context manager."""
        error_string = "Can't use {} as a context manager."
        raise TypeError(error_string.format(self.__class__.__name__))

    def __exit__(self, *args):
        """Do nothing."""
        pass


class Paragraph:
    """Acts as a body of text, with newline characters between each segment."""

    def __init__(self):
        """Initialize an empty paragraph."""
        super().__init__()
        self._text = []

    def __iter__(self):
        """Iterate over the text segments."""
        return iter(self._text)

    def __len__(self):
        """Return the number of text segments stored."""
        return len(self._text)

    def write(self, *args, **kwargs):
        """Append the given text segment or parameters to the paragraph."""
        if len(args) == 1:
            self._text.append(args[0])
        else:
            self._text.append(args)

    def __str__(self):
        """Return all text segments, joined with newlines."""
        return '\n'.join(map(str, self))

    def __enter__(self):
        """Raise an error; cannot be used as a context manager."""
        error_string = "Can't use {} as a context manager."
        raise TypeError(error_string.format(self.__class__.__name__))

    def __exit__(self, *args):
        """Do nothing."""
        pass


class Registry:
    """
    Manages a single section in the document preamble.

    Entries can be registered under a unique key.
    Each entry is formatted in a consistent style and written to its own line.
    The registry can then be written to the document preamble.
    """

    def __init__(self):
        """Create an empty ``Registry``."""
        super().__init__()
        self._entries = OrderedDict()

    def __iter__(self):
        """Iterate over the keys in the registry."""
        return iter(self._entries)

    def __contains__(self, item):
        """Determine if a given key is contained in the registry."""
        return item in self._entries

    def __len__(self):
        """Return the number of registry entries."""
        return len(self._entries)

    def items(self):
        """Return an iterator over the key-entry pairs in the registry."""
        return self._entries.items()

    def register(self, key, value=None):
        """Register an entry under the given key, if not already present."""
        self._entries.setdefault(key, value)

    # Should be overridden in subclasses
    @staticmethod
    def _entry_line(entry, value) -> str:
        """Format a single registration entry as text."""
        return entry

    # Generally should not be overridden
    # Override _entry_line instead
    def __str__(self):
        """
        Format the entire registry as a string.

        Each registry key-entry pair is formatted using ``_entry_line``,
        and written to its own line.
        This method should not be overridden; override ``_entry_line`` instead.
        """
        return '\n'.join(str(self._entry_line(key, value))
                         for key, value in self.items())
