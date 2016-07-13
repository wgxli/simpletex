import simpletex
from simpletex import usepackage, add_registry
from simpletex.base import Environment, Command
from simpletex.formatting import Style
from simpletex.formatting.core import Indent
from simpletex.registry.formatting import TitleFormatRegistry

class Document(Environment):
    def __init__(self, documentClass='article', size='12pt'):
        super().__init__('document')
        simpletex._CONTEXT.classDeclaration = Command('documentclass', [documentClass], size)
        usepackage('inputenc', 'utf8')
        usepackage('xltxtra')


class Title(Environment):
    heading = Style(inline=True)
    def __init__(self, command_name, name):
        super().__init__()
        self._heading = Command(command_name, [name])
        add_registry('titleFormat', TitleFormatRegistry())
        
    def format_text(self, text) -> str:
        if self.heading:
            usepackage('titlesec')
            simpletex._CONTEXT.titleFormat.register(self.command_name, self.heading)
        return '\n'.join(map(str, [self._heading,
                                   Indent()(text)]))
    
    @property
    def command_name(self):
        return self._heading.name
    @command_name.setter
    def command_name(self, value):
        self._heading.name = value

        
class Section(Title):
    heading = Style(inline=True)
    def __init__(self, name):
        super().__init__('section', name)


class Subsection(Title):
    heading = Style(inline=True)
    def __init__(self, name):
        super().__init__('subsection', name)
    
