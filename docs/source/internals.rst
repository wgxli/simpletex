Internals
=========

This section details the internals of simpletex.

The ``Formatter`` Class
-----------------------

The core of simpletex is the ``Formatter`` class, located in ``simpletex.core``. Instances of ``Formatter`` (or its subclasses) format text, and can either be called (like a function, passing text as the argument), or used as a context manager in a ``with`` statement (in which case all text written in the ``with`` block will be passed to the ``Formatter`` upon exit). With a few exceptions, every class in simpletex is a ``Formatter``.
