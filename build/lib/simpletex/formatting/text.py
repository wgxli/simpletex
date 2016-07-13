from latex.core import Formatter
from latex.base import Command, Environment

class Italics(Formatter):
    def __init__(self, inline=False):
        super().__init__()
        self._inline = inline
    def format_text(self, text: str) -> str:
        if self._inline:
            return '{}{}'.format(Command('itshape'), text)
        else:
            return Command('textit', [text])

class Centering(Environment):
    def __init__(self, inline=False):
        super().__init__('center')
        self._inline = inline
    def format_text(self, text: str) -> str:
        if self._inline:
            return '{}{}'.format(Command('centering'), text)
        else:
            return super().format_text(text)
