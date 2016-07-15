"""
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

__all__ = ('Document', 'Section', 'Subsection')


class Document(Environment):
    """A class which manages a LaTeX document.

    Upon instantiation, sets the input encoding to UTF-8
    and declares the document class.
    This class does NOT manage the preamble
    (imports, newcommand declarations, etc.).
    The preamble is managed by the `simpletex.Preamble` class.
    """

    def __init__(self, document_class: str = 'article', size: str = '12pt'):
        """
        Create an empty document using the given document class and font size.

        document_class : str
            The LaTeX document class name to use.
        size : str
            The default font size to use.
        """
        super().__init__('document')
        simpletex._CONTEXT.classDeclaration = Command('documentclass',
                                                      [document_class],
                                                      size)
        usepackage('inputenc', 'utf8')


class Title(Environment):
    heading = Style(inline=True)

    def __init__(self, command_name: str, name: str):
        super().__init__()
        self._heading = Command(command_name, [name])
        add_registry('titleFormat', TitleFormatRegistry())

    def _format_text(self, text) -> str:
        if self.heading:
            usepackage('titlesec')
            simpletex._CONTEXT.titleFormat.register(self.command_name,
                                                    self.heading)
        return '\n'.join(map(str, [self._heading,
                                   Indent()(text)]))

    @property
    def command_name(self) -> str:
        return self._heading.name

    @command_name.setter
    def command_name(self, value):
        self._heading.name = value


class Section(Title):
    """Represents a LaTeX section."""

    heading = Style(inline=True)
    """
    Section heading style.
    If formatting is applied, a global section style
    will be registered, and the 'titlesec' package will be imported.
    """

    def __init__(self, name: str):
        """
        Create an empty section with the given name.

        name : str
            The section name.
        """
        super().__init__('section', name)


class Subsection(Title):
    """Represents a LaTeX subsection."""

    heading = Style(inline=True)
    """
    Subsection heading style.
    If formatting is applied, a global subsection style
    will be registered, and the 'titlesec' package will be imported.
    """

    def __init__(self, name: str):
        """
        Create an empty subsection with the given name.

        name : str
            The subsection name.
        """
        super().__init__('subsection', name)
