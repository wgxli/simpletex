from simpletex.core import Formatter


class Indent(Formatter):
    def __init__(self):
        super().__init__()

    def __call__(self, text) -> str:
        lines = str(text).split('\n')
        return '\n'.join(map(self._tab_line, lines))

    @staticmethod
    def _tab_line(text):
        if text != '':
            text = '\t' + text
        return text
