"""
This module provides formatting registries to use in the document preamble.

..  :copyright: (c) 2016 by Samuel Li.
    :license: GNU GPLv3, see License for more details.
"""

from simpletex.core import Registry
from simpletex.base import Command

__all__ = ()


class FontRegistry(Registry):
    def __init__(self):
        super().__init__()

    @staticmethod
    def _entry_line(font, _):
        return "{}{}".format(Command('newfontfamily'),
                             Command(FontRegistry._font_name(font),
                                     [font],
                                     Mapping='tex-text'))

    @staticmethod
    def _font_name(font):
        return font.replace(" ", "")


class TitleFormatRegistry(Registry):
    def __init__(self):
        super().__init__()

    @staticmethod
    def _entry_line(title_name, formatting):
        return "{}".format(Command('titleformat*',
                           [Command(title_name),
                            formatting('')]))
