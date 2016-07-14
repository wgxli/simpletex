from simpletex.core import Formatter


class Style(Formatter):
    def __init__(self, inline=False):
        super().__init__()
        self._formatters = []
        self._inline = inline

    def apply(self, formatter):
        if not isinstance(formatter, Formatter):
            error_string = '{} is not a Formatter.'
            raise TypeError(error_string.format(formatter.__class__.__name__))
        formatter._inline = self._inline
        self._formatters.append(formatter)

    def format_text(self, text) -> str:
        for formatter in self._formatters:
            text = formatter(text)
        return text

    def __bool__(self):
        return bool(self._formatters)

    def __repr__(self):
        return '{}{}'.format(self.__class__.__name__, self._formatters)
