.. image:: https://badge.fury.io/py/simpletex.svg
    :target: https://badge.fury.io/py/simpletex

.. image:: https://readthedocs.org/projects/simpletex/badge/?version=latest
    :target: http://simpletex.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status
	
.. image:: https://travis-ci.org/wgxli/simpletex.svg?branch=master
    :target: https://travis-ci.org/wgxli/simpletex
    :alt: Build Status
    
.. image:: https://coveralls.io/repos/github/wgxli/simpletex/badge.svg?branch=master
   :target: https://coveralls.io/github/wgxli/simpletex?branch=master
   :alt: Coverage Status
	
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
