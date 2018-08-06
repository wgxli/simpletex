from simpletex import write, dump
from simpletex.sequences import Description

with Description():
    write('asdf', 'fdsa')
print(dump())
