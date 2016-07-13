"""
Document Structure
==================
This module provides utilities to define a document's basic structure.

..  :copyright: (c) 2016 by Samuel Li.
    :license: GNU GPLv3, see License for more details.
"""

import simpletex
from simpletex import usepackage, add_registry
from simpletex.base import Environment, Command
from simpletex.formatting import Style
from simpletex.formatting.core import Indent
from simpletex.registry.formatting import TitleFormatRegistry

__all__ = ['Document', 'Section', 'Subsection']


class Document(Environment):
    """A class which manages a LaTeX document.

    This class does NOT manage the preamble
    (imports, newcommand declarations, etc.).
    The preamble is managed by the `simpletex.Preamble` class.
    Upon instantiation, loads the input encoding to UTF-8
    and declares the document class.
    """
    def __init__(self, documentClass='article', size='12pt'):
        """
        documentClass : str
            LaTeX class name
        size : str
            default font size
        """
        super().__init__('document')
        simpletex._CONTEXT.classDeclaration = Command('documentclass',
                                                      [documentClass],
                                                      size)
        usepackage('inputenc', 'utf8')


class Title(Environment):
    heading = Style(inline=True)

    def __init__(self, command_name, name):
        super().__init__()
        self._heading = Command(command_name, [name])
        add_registry('titleFormat', TitleFormatRegistry())

    def format_text(self, text) -> str:
        if self.heading:
            usepackage('titlesec')
            simpletex._CONTEXT.titleFormat.register(self.command_name,
                                                    self.heading)
        return '\n'.join(map(str, [self._heading,
                                   Indent()(text)]))

    @property
    def command_name(self):
        return self._heading.name

    @command_name.setter
    def command_name(self, value):
        self._heading.name = value


class Section(Title):
    """Represents a LaTeX section."""
    heading = Style(inline=True)

    def __init__(self, name):
        """
        name : str
            section name
        """
        super().__init__('section', name)


class Subsection(Title):
    """Represents a LaTeX subsection."""
    heading = Style(inline=True)

    def __init__(self, name):
        """
        name : str
            subsection name
        """
        super().__init__('subsection', name)
