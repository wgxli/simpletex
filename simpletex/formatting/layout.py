from simpletex import usepackage
from simpletex.base import Command, Environment


class Centering(Environment):
    def __init__(self, inline=False):
        super().__init__('center')
        self._inline = inline

    def format_text(self, text: str) -> str:
        if self._inline:
            return '{}{}'.format(Command('centering'), text)
        else:
            return super().format_text(text)


class Columns(Environment):
    def __init__(self, number):
        super().__init__('multicols')
        usepackage('multicol')
