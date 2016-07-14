Tutorial
========

This tutorial covers the fundamentals, basic usage, advanced features, and third-party support of simpletex.
For further usage examples, please see the :doc:`examples`.

Fundamentals
------------
The core of simpletex is the ``Formatter`` class; nearly all simpletex classes derive from this base class.
Formatters apply formatting to (mostly) text. For example, the ``Italics`` formatter italicizes text.
Formatters can be used by calling a ``Formatter`` instance.

.. code-block:: python

	>>> from simpletex.formatting.text import Italics
	>>> print(Italics()('Hello World!'))
	\textit{Hello World!}
	
Formatter instances can also be used as context managers.
Upon exit of the ``with`` block, all written text is passed to the formatter.

.. code-block:: python

	>>> from simpletex import write, dump
	>>> with Italics():
			write('Hello')
			write('World')
	>>> dump()
	'\\textit{Hello\nWorld}'

Basic Usage
-----------
Creating Our First Document
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

	from simpletex import write, save
	from simpletex.document import Document

	with Document():
		write('Hello World!')

	save('hello_world.tex')

That wasn't so hard, was it?

Sections and Formatting
~~~~~~~~~~~~~~~~~~~~~~~
Let's create a document with two sections:

.. code-block:: python

	from simpletex import write, save
	from simpletex.document import Document, Section

	with Document():
		with Section('A'):
			write('First Section Text')
		with Section('B'):
			write('Second Section Text')

	save('section_basics.tex')
	
Easy enough. Let's italicize all the section headings:

.. code-block:: python

	from simpletex import write, save
	from simpletex.document import Document, Section
	from simpletex.formatting.text import Italics
	
	Section.heading.apply(Italics())
	
	with Document():
		with Section('A'):
			write('First Section Text')
		with Section('B'):
			write('Second Section Text')

	save('section_basics.tex')
	
Pretty good for two additional lines.

In the previous example, ``Section.heading`` is a ``Style``:
a ``Formatter`` which allows many other Formatters to be conveniently comibined.
