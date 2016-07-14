"""
Font Formatting
===============
This module provides utilities to change the font and size of text.

..  :copyright: (c) 2016 by Samuel Li.
    :license: GNU GPLv3, see License for more details.
"""

import simpletex
from simpletex import usepackage, add_registry
from simpletex.core import Formatter
from simpletex.base import Command, Brace
from simpletex.registry.formatting import FontRegistry

__all__ = ['Font', 'SizeSelector']


class SizeSelector(Formatter):
    """
    Changes the size of text.
    Imports package 'anyfontsize' on instantiation.
    """
    def __init__(self, size, skip=None):
        super().__init__()
        self.size = size
        self.skip = skip
        usepackage('anyfontsize')

    def _format_text(self, text) -> str:
        if self.size is None or self.skip is None:
            return text
        return '{}{}'.format(Command('fontsize', [self.size, self.skip]),
                             text)


class FontSelector(Formatter):
    def __init__(self, name: str):
        super().__init__()
        self.name = name
        add_registry('fontRegistry', FontRegistry())
        simpletex._CONTEXT.fontRegistry.register(self.name)
        usepackage('fontspec')
        usepackage('xltxtra')

    def _format_text(self, text) -> str:
        font_tex_name = simpletex._CONTEXT.fontRegistry._font_name(self.name)
        return '{} {}'.format(Command(font_tex_name),
                              text)


class Font(Formatter):
    """
    Changes the font face (and optionally the size) of text.
    Imports packages 'fontspec' and 'xltxtra' on instantiation.
    If used, the document must be processed with XeTeX
    or another font-aware TeX processor.
    """
    def __init__(self,
                 name: str,
                 size: int = None,
                 skip: int = None,
                 inline: bool = False):
        """
        name : str
            The name of the font to use.
        """
        super().__init__()
        self.name = name
        self.size = size
        if skip is None and size is not None:
            self.skip = int(size*1.3)
        else:
            self.skip = skip
        self._inline = inline

    def _format_text(self, text) -> str:
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
