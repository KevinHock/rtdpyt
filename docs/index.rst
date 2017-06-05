Welcome to pyt's documentation!
===============================

`pyt`_ is static analysis tool for detecting security vulnerabilities in Python3 web applications.
It uses the `ast`_ module to parse Python and then performs a [variant of reaching definitions](http://projekter.aau.dk/projekter/files/239563289/final.pdf#page=57) to track taint from source to sink.

.. _pyt: https://github.com/python-security/pyt
.. _ast: https://docs.python.org/3/library/ast.html

The main documentation for the tool is organized into a few sections:

* :ref:`user-docs`
* :ref:`about-docs`
* :ref:`dev-docs`

.. _user-docs:

.. toctree::
   :maxdepth: 2
   :caption: User Documentation

   getting_started
   features
   faq
   support

.. _about-docs:

.. toctree::
   :maxdepth: 2
   :caption: About pyt

   story
   maturity
   roadmap
   contribute
   team
   related_work

.. _dev-docs:

.. toctree::
   :maxdepth: 2
   :caption: Developer Documentation

   install
   tests
   docs
   architecture
   details

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
