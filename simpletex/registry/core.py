from simpletex.core import Registry
from simpletex.base import Command


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
