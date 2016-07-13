simpletex: Simple LaTeX Documents
=================================

simpletex is a Python library for automatically generating LaTeX documents. It is extremely easy to use:

.. code-block:: python

    from simpletex import write, save
    from simpletex.document import Document, Section, Subsection
    
    with Document(size='11pt'):
        with Section('Section Name'):
            with Subsection('Subsection Name'):
                write('Hello World!')
    
    save('filename.tex')

For a quick introduction to using simpletex, please refer to the :doc:`tutorial`. For an overview of simpletex's functionality, please see the :doc:`examples`.

Getting Started
---------------
.. toctree::
    :maxdepth: 1

    install
    tutorial
    
Advanced Usage
--------------
.. toctree::
    :maxdepth: 1

    internals
