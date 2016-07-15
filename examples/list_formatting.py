from simpletex import write, save
from simpletex.document import Document, Section, Subsection
from simpletex.formatting.text import (Bold, Italics, Underline,
                                       Emphasis, SmallCaps)
from simpletex.sequences import OrderedList, UnorderedList

UnorderedList.bullet = '>'

with Document(size='11pt'):
    with Section('Section Name'):
        with UnorderedList():
            write(Bold()('Bold Text'))
            write(Italics()('Italic Text'))
            write(Underline()('Underlined Text'))
            with Underline():
                write('More Underlined Text')
        with Subsection('Subsection Name'):
            write('The quick brown fox jumps over the lazy dog.')
            with OrderedList():
                write(Emphasis()('Emphasized Text'))
                write(SmallCaps()('Small Caps'))

save('filename.tex')
