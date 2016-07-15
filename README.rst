.. image:: https://img.shields.io/pypi/v/simpletex.svg
    :target: https://pypi.python.org/pypi/simpletex
    :alt: PyPI

.. image:: https://readthedocs.org/projects/simpletex/badge/?version=latest
    :target: http://simpletex.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status
	
.. image:: https://travis-ci.org/swe100/simpletex.svg?branch=master
    :target: https://travis-ci.org/swe100/simpletex
	:alt: Build Status

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
    
Full documentation can be found at http://simpletex.readthedocs.io/.
