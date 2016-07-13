"""This module provides utilities to perform basic text formatting."""

from simpletex.core import Formatter
from simpletex.base import Command, Environment

class SimpleFormatter(Formatter):
    def __init__(self, command_name, inline_name, inline=False):
        super().__init__()
        self.command_name = command_name
        self.inline_name = inline_name
        self._inline = inline
    def format_text(self, text: str) -> str:
        if self._inline:
            return '{}{}'.format(Command(self.inline_name),
                                 text)
        else:
            return Command(self.command_name, [text])


class Bold(SimpleFormatter):
    def __init__(self, inline=False):
        super().__init__('textbf', 'bfshape', inline)

class Italics(SimpleFormatter):
    def __init__(self, inline=False):
        super().__init__('textit', 'itshape', inline)

class Underline(SimpleFormatter):
    def __init__(self, inline=False):
        super().__init__('underline', 'underline', inline)

class SmallCaps(SimpleFormatter):
    def __init__(self, inline=False):
        super().__init__('textsc', 'scshape', inline)

class Emphasis(SimpleFormatter):
    def __init__(self, inline=False):
        super().__init__('emph', 'em', inline)
