import simpletex
from simpletex import usepackage, add_registry
from simpletex.core import Formatter
from simpletex.base import Command, Brace
from simpletex.registry.formatting import FontRegistry

class SizeSelector(Formatter):
    def __init__(self, size, skip):
        super().__init__()
        self.size = size
        self.skip = skip
        usepackage('anyfontsize')
        
    def format_text(self, text) -> str:
        if self.size is None or self.skip is None:
            return text
        return '{}{}'.format(Command('fontsize', [self.size, self.skip]),
                              text)

class FontSelector(Formatter):
    def __init__(self, name):
        super().__init__()
        self.name = name
        add_registry('fontRegistry', FontRegistry())
        simpletex._CONTEXT.fontRegistry.register(self.name)
        usepackage('fontspec')
        
    def format_text(self, text) -> str:
        font_tex_name = simpletex._CONTEXT.fontRegistry._font_name(self.name)
        return '{} {}'.format(Command(font_tex_name),
                              text)

class Font(Formatter):
    def __init__(self, name, size=None, skip=None, inline=False):
        super().__init__()
        self.name = name
        self.size = size
        if skip is None and size is not None:
            self.skip = int(size*1.3)
        else:
            self.skip = skip
        self._inline = inline
        
    def format_text(self, text: str) -> str:
        font_string = FontSelector(self.name)(text)
        size_string = SizeSelector(self.size, self.skip)(font_string)
        if self._inline:
            return size_string
        else:
            return Brace()(size_string)

    def __repr__(self):
        return '{}(name={}, size={}, skip={})'.format(self.__class__.__name__,
                                                      self.name,
                                                      self.size,
                                                      self.skip)
