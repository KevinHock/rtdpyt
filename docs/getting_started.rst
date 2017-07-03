Getting Started
===============

This document will show you how to get started using PyT.

Install
--------------------------------------

       1. git clone https://github.com/python-security/pyt.git
       2. python setup.py install
       3. pyt -h


Usage from Source
--------------------------------------

Using it like a user ``python -m pyt -f example/vulnerable_code/XSS_call.py save -du``

Running the tests ``python -m tests``

Running an individual test file ``python -m unittest tests.import_test``

Running an individual test ``python -m unittest tests.import_test.ImportTest.test_import``