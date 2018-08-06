"""
This module contains useful utilities to build higher-level formatters.

..  :copyright: (c) 2016 by Samuel Li.
    :license: GNU GPLv3, see License for more details.
"""


from simpletex.core import Text, Formatter
from simpletex.formatting.core import Indent

__all__ = ('Command')


class Brace(Formatter):
    def __call__(self, *args):
        return ''.join('{{{}}}'.format(arg) for arg in args)


class OptionFormatter(Formatter):
    def __call__(self, *args, **kwargs):
        kwarg_strings = ['{}={}'.format(k, v) for k, v in kwargs.items()]
        option_string = ', '.join(list(args) + kwarg_strings)
        if option_string:
            return '[{}]'.format(option_string)
        else:
            return ''


class Command(Text):
    """Represents a single LaTeX command."""

    def __init__(self, name: str, arguments=(), *args, **kwargs):
        """
        Create a command with the given name, arguments, and options.

        name : str
            The name of the command.
        arguments : list of str
            The arguments of the LaTeX command.
            Will be formatted with curly braces.
        args
            Optional parameters for the command.
            Will be placed in square brackets before the main arguments.
        kwargs
            Optional keyword parameters for the command.
            Will be placed in square brackets before the main arguments,
            formatted as ``key=value``.
        """
        super().__init__()
        self.name = name
        self.arguments = list(arguments)
        self.options = (args, kwargs)

    def __str__(self):
        """Format the command as LaTeX."""
        return r'\{}{}{}'.format(self.name,
                                 OptionFormatter()(*self.options[0],
                                                   **self.options[1]),
                                 Brace()(*self.arguments))


class Environment(Formatter):
    def __init__(self, name=None, *args):
        super().__init__()
        if name is not None:
            # [name, *args] not supported in Python 3.4 and below
            self.header = Command('begin', [name] + list(args))
            self.footer = Command('end', [name])

    def _format_text(self, text) -> str:
        try:
            # Test for header and footer presence
            self.header
            self.footer
        except AttributeError as e:
            error_string = 'No name specified for {}.'
            class_name = self.__class__.__name__
            raise ValueError(error_string.format(class_name)) from e
        return '\n'.join(map(str, [self.header,
                                   Indent()(text),
                                   self.footer]))
