from simpletex.core import Text, Formatter
from simpletex.formatting.core import Indent


class Brace(Formatter):
    def __init__(self):
        super().__init__()

    def __call__(self, *args):
        return ''.join('{{{}}}'.format(arg) for arg in args)


class OptionFormatter(Formatter):
    def __init__(self):
        super().__init__()

    def __call__(self, *args, **kwargs):
        kwarg_strings = ['{}={}'.format(k, v) for k, v in kwargs.items()]
        option_string = ', '.join(list(args) + kwarg_strings)
        if option_string:
            return '[{}]'.format(option_string)
        else:
            return ''


class Command(Text):
    def __init__(self, name, arguments=[], *args, **kwargs):
        super().__init__()
        self.name = name
        self.arguments = arguments
        self.options = [args, kwargs]

    def __str__(self):
        return r'\{}{}{}'.format(self.name,
                                 OptionFormatter()(*self.options[0],
                                                   **self.options[1]),
                                 Brace()(*self.arguments))


class Environment(Formatter):
    def __init__(self, name=None):
        super().__init__()
        if name is not None:
            self.header = Command('begin', [name])
            self.footer = Command('end', [name])

    def _format_text(self, text) -> str:
        return '\n'.join(map(str, [self.header,
                                   Indent()(text),
                                   self.footer]))
