simpletex: Simple LaTeX Documents
=================================

simpletex is a Python library for automatically generating LaTeX documents. It is extremely easy to use:

.. code-block:: python

    >>> from simpletex import write
    >>> from simpletex.document import Document, Section, Subsection
    >>> with Document(size='11pt') as doc:
            with Section('Section Name'):
                with Subsection('Subsection Name'):
                    write('Hello World!')
    >>> doc.save("filename.tex")
    
Contents:

.. toctree::
   :maxdepth: 2



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

