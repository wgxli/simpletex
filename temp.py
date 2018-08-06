from simpletex import write, dump
from simpletex.document import Document

with Document():
    write('asdf')
print(dump())
