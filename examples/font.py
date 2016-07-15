from simpletex import write, write_break, save, usepackage
from simpletex.document import Document, Section, Subsection
from simpletex.formatting import Style
from simpletex.formatting.font import Font
from simpletex.formatting.text import Italics, SmallCaps
from simpletex.formatting.layout import Centering

title = Style()
title.apply(Font('Bebas Neue Bold', size=40))

subtitle = Style()
subtitle.apply(Font('Times New Roman', size=11))

Section.heading.apply(Font('Open Sans Semibold', size=16))

Subsection.heading.apply(Font('Open Sans Semibold', size=12))
Subsection.heading.apply(Italics())
Subsection.heading.apply(Centering())

usepackage('geometry', margin='0.5in')
with Document(size='11pt'):
    with Centering():
        write_break(title('Example Title Text'))
        with subtitle:
            write_break("Example Subtitle Text")
            write_break("More Subtitle Text")
    with Section('Section Name'):
        write('Example section text.')
        write(SmallCaps()('Lorem ipsum dolor si amet.'))
        with Subsection('Subsection Name'):
            write('Hello World!')

save('filename.tex')
