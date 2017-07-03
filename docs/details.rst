How It Works
==========================

* What is an AST?
	The wikipedia page of `abstract syntax tree`_ is pretty clear. All the different kinds of nodes in Python are documented on `Green Tree Snakes`_,
	
* What is the best beginner friendly resource to learning about dataflow analysis?
	Probably just `Engineering a Compiler`_. All you need to know at a minimum to understand PyT is reaching definitions.

* What is reaching definitions?
	The wikipedia page of `reaching definitions analysis`_ is pretty clear. It is a type of dataflow analysis.

* What is liveness analysis?

* What does fixed point mean?
	Iterate and perform this dataflow analysis until nothing changes. The until nothing changes part is what is known as a fixed point.

* How does fixpointmethod affect constraint table?
	It depends on the dataflow analysis, but 

* What is a lattice?
	A lattice is just a partially ordered set that sounds fancy and looks pretty in papers. For example, in the case of reaching definitions, the lattice is made up of all the assignments in the program.

* What design patterns are used in the PyT codebase?
	The template pattern is used when deciding what analysis to use.
	The visitor pattern is used throughout the codebase, when visiting the different nodes of the AST.

.. _abstract syntax tree: https://en.wikipedia.org/wiki/Abstract_syntax_tree
.. _Green Tree Snakes: http://greentreesnakes.readthedocs.io/en/latest/nodes.html

.. _Engineering a Compiler: https://www.amazon.com/Engineering-Compiler-Second-Keith-Cooper/dp/012088478X
.. _reaching definitions analysis: https://en.wikipedia.org/wiki/Reaching_definition#As_analysis
