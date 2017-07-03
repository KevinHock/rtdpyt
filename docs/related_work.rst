Related Work
==========================

Related Projects
---------------------------

* `Bandit`_
	Bandit was a tool made by a `few people at OpenStack`_ with the same purpose of PyT in mind, the main difference is that Bandit doesn't track the flow of data and PyT does, so it's closer to a grep ish pre-commit hook to e.g. ban urllib2 and open etc. and suggest Advocate and a secure open wrapper instead. The sinks, formatters and UI are where it shines.

* JunkHacker
	Written by `Kevin Hock`_ and had an incredibly bad design, it analyzed Python bytecode using `equip`_ and tracked taint by depth-first searching through basic block's via a bytecode interpreter heavily adopted from `Byterun`_. It dealth with path-explosion via a crazy `buddy system`_ and being that many byecode instructions e.g. exceptions do not work on the basic block level, work arounds were gruesome. The `buddy system`_ worked by marking each node that diverged with the node that it's children converged at. This was both less efficient than unioning predecessors like PyT and more complicated. It is not open-source because of how ugly it is.

* `Focuson`_
	Written by `Collin Greene`_ of Uber, similar to PyT it uses the `ast module`_ but unlike PyT it tracks dataflow using path-insensitive backwards slicing. Path explosion is not a problem because it is path-insensitive, but that causes it to have more false-positives than PyT.

* `PyExZ3`_
	A dynamic symbolic execution framework for Python, potentially useful for taint tracking if it can `solve string constraints`_, which there is experimental support for in a `fork`_. "A novel aspect of the rewrite is to rely solely on Python's operator overloading to accomplish all the interception needed for symbolic execution." `Joseph Near`_ did this before them, but it is interesting work nevertheless.

* `DARLAB Work`_
	Has great `alias analysis work`_, by `Michael Gorbovitski`_ et al. It would be quite performance intensive to add to a security tool and may or may not be that helpful for reducing false positives, but is quite impressive work regardless.

* `RIPS`_ (PHP)
	The latest versions, the useful ones, are closed-source, as the author `Johannes Dahse`_ has gone commercial. This is unfortunate and it seems like the most advanced tool in this category as far as we know because it can find `second order`_ vulnerabilities. The old unsophisticated open-source version is `here`_.

* `Brakeman`_ (Rails)
	Written by `Justin Collins`_, it is written in Ruby and made for Rails. I'm not exactly sure how it works, but it does do something like reaching definitions.

* `Dawnscanner`_ (Ruby)
	Written by `Paolo Perego`_, I'm not exactly sure how it works.

* `Joseph Near`_ et al. (Rails)
	Joseph has a lot of interesting work I would like to summarize.

.. _Bandit: https://github.com/openstack/bandit
.. _few people at OpenStack: https://wiki.openstack.org/wiki/Security/Projects/Bandit#Team

.. _Kevin Hock: https://twitter.com/kevinhock2
.. _equip: https://github.com/neuroo/equip
.. _Byterun: https://github.com/nedbat/byterun
.. _buddy system: https://gist.github.com/KevinHock/7fb0a41ec7bcb77d3422ebe8a4b83e84

.. _Focuson: https://github.com/uber/focuson
.. _Collin Greene: https://twitter.com/libber
.. _ast module: https://docs.python.org/3/library/ast.html

.. _PyExZ3: https://github.com/thomasjball/PyExZ3
.. _solve string constraints: https://github.com/thomasjball/PyExZ3/issues/23
.. _fork: https://github.com/GroundPound/PyExZ3

.. _DARLAB Work: https://github.com/mickg10/DARLAB
.. _Michael Gorbovitski: https://www.linkedin.com/in/michaelgorbovitski
.. _alias analysis work: http://www3.cs.stonybrook.edu/~liu/papers/Alias-DLS10.pdf

.. _RIPS: https://www.ripstech.com/
.. _Johannes Dahse: https://twitter.com/FluxReiners
.. _here: https://github.com/robocoder/rips-scanner
.. _second order: https://www.usenix.org/system/files/conference/usenixsecurity14/sec14-paper-dahse.pdf

.. _Brakeman: https://github.com/presidentbeef/brakeman
.. _Justin Collins: https://twitter.com/presidentbeef

.. _Dawnscanner: https://github.com/thesp0nge/dawnscanner
.. _Paolo Perego: https://twitter.com/thesp0nge

.. _Joseph Near: http://people.eecs.berkeley.edu/~jnear/


Related Papers
---------------------------

* `Schwarzbach static analysis notes`_ The PyT thesis is heavily influenced by these notes, they're a pretty good resource for learning dataflow analysis. Other good resources include `Engineering a Compiler`_, `Advanced Compiler Design and Implementation`_ and `Data Flow Analysis\: Theory and Practice`_.

* `Alias Analysis for Optimization of Dynamic Languages`_

* `Static Detection of Second Order Vulnerabilities in Web Applications`_
	A simple intuitive idea, but complex to implement. Unlike PyT they use summaries instead of inlining, summaries are sort of required to implement the idea, unless you wrote results somewhere and ran the tool again with those results in a dirty hack.
	The main hard-parts with implementing this idea with PyT will be (1) re-writing to use summaries, (2) writing code that deals with this part of the paper "SQL has different syntactical forms of writing data to a table. Listing 1 shows three different ways to perform the same query". Aside from the examples given in the paper, some other examples of multi-step exploits are as follows. Tracking from bad RNG to store in location A to HTTP response, then seeing where a taint value is checked against location A.

	In my opinion, the best ROI in the Python world would be to implement this for the Django ORM or SQLAlchemy since they seem to be the most widely used.
 
* `Finding Security Bugs in Web Applications using a Catalog of Access Control Patterns`_

* `Derailer Interactive Security Analysis for Web Applications`_

* `Practical Static Analysis of JavaScript Applications in the Presence of Frameworks and Libraries`_
	There are 3 ways of handling blackbox calls between source and sink, to basically answer the questions that a proper summary does, e.g. if argument A is tainted, does this call return a tainted value? This can be dealth with via (1) hard-coded mapping, (2) pip install, see if Python code or, (3) possibly this paper. I suspect long-term, some combination of 1 and 2 will be done with PyT. If we just ask the user, "Hey, does this call propagate taint?" and we remember the answer, it would be easy enough for the user to use the tool.

.. _Schwarzbach static analysis notes: http://lara.epfl.ch/w/_media/sav08:schwartzbach.pdf
.. _Engineering a Compiler: https://www.amazon.com/Engineering-Compiler-Second-Keith-Cooper/dp/012088478X
.. _Advanced Compiler Design and Implementation: https://www.amazon.com/Advanced-Compiler-Design-Implementation-Muchnick/dp/1558603204
.. _Data Flow Analysis\: Theory and Practice: https://www.amazon.com/Data-Flow-Analysis-Theory-Practice/dp/0849328802

.. _Alias Analysis for Optimization of Dynamic Languages: http://www3.cs.stonybrook.edu/~liu/papers/Alias-DLS10.pdf
.. _Static Detection of Second Order Vulnerabilities in Web Applications: https://www.usenix.org/system/files/conference/usenixsecurity14/sec14-paper-dahse.pdf
.. _Finding Security Bugs in Web Applications using a Catalog of Access Control Patterns: https://dspace.mit.edu/openaccess-disseminate/1721.1/102281
.. _Derailer Interactive Security Analysis for Web Applications: http://people.eecs.berkeley.edu/~jnear/papers/ase14.pdf
.. _Practical Static Analysis of JavaScript Applications in the Presence of Frameworks and Libraries: https://www.doc.ic.ac.uk/~livshits/papers/tr/jscap_tr.pdf
