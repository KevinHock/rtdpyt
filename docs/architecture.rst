Architecture
============

A great overview from the original thesis is below:

.. image:: img/overview.png

1. Source code to AST
2. AST to CFG
3. CFG entered into a Framework Adaptor
4. Running a fixpoint algorithm on the result of 3
5. Spit out all the vulnerabilities.

I'll go through each of these steps in depth and walk through where in the code they happen.

Source code to AST
---------------------------

This is by far the easiest step, as it is done for us by the `ast`_ module, the only place where we perform parsing is the `generate_ast` function in the `ast_helper\.py`_ file, where we just write :python:`ast.parse(f.read())` on a file. The result is a tree of objects whose classes all inherit from `ast\.AST`_.

.. _ast: https://docs.python.org/3/library/ast.html
.. _ast_helper\.py: https://github.com/python-security/pyt/blob/master/pyt/ast_helper.py
.. _ast\.AST: https://docs.python.org/3/library/ast.html#ast.AST

AST to CFG
---------------------------

This is mostly performed by a class that inherits from `ast\.NodeVisitor`_ 

.. _ast\.NodeVisitor: https://github.com/python/cpython/blob/master/Lib/ast.py#L224

.. role:: python(code)
   :language: python