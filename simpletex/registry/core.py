"""
This module provides basic registries to use in the document preamble.

..  :copyright: (c) 2016 by Samuel Li.
    :license: GNU GPLv3, see License for more details.
"""

from simpletex.core import Registry
from simpletex.base import Command

__all__ = ()


class ImportRegistry(Registry):
    def __init__(self):
        super().__init__()

    @staticmethod
    def _entry_line(entry, value):
        args, kwargs = value
        return Command('usepackage',
                       [entry],
                       *args,
                       **kwargs)


class CommandDefinitionRegistry(Registry):
    def __init__(self):
        super().__init__()

    @staticmethod
    def _entry_line(entry, definition):
        return Command('newcommand',
                       [Command(entry), definition])
