Tutorial
========

This tutorial covers the basic usage, advanced features, and third-party support of simpletex. For further usage examples, please see the :doc:`examples`.


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
	
Easy enough. Let's add italicize all the section headings:

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
	
Pretty good for two more lines.
