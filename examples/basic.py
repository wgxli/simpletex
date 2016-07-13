from simpletex import write, save
from simpletex.document import Document, Section, Subsection

with Document(size='11pt'):
    with Section('Section Name'):
        with Subsection('Subsection Name'):
            write('Hello World!')

save('filename.tex')
