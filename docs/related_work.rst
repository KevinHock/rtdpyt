Related Projects
==========================================

* `Bandit`_
	Bandit was a tool made by a few people at OpenStack with the same purpose of PyT in mind, the main difference is that Bandit doesn't track the flow of data and PyT does, so it's closer to a grep ish pre-commit hook to e.g. ban urllib2 and open etc. and suggest Advocate and a secure open wrapper instead. The sinks, formatters and UI are the strong points.

.. _junkhacker:
* JunkHacker
	JunkHacker was written by `Kevin Hock`_ and had an incredibly bad design, it analyzed Python bytecode using `equip`_ and tracked taint by depth-first searching through basic block's via a bytecode interpreter heavily adopted from `Byterun`_. It dealth with path-explosion via a crazy `buddy system`_ and being that many byecode instructions e.g. exceptions do not work on the basic block level, work arounds were gruesome. The `buddy system`_ worked by marking each node that diverged with the node that it's children converged, and keeping a stack of buddies on in the code that performed DFS. This was both less efficient than unioning predecessors like PyT and more complicated. It is not open-source because of how ugly it is.

.. _Focuson:
* `Focuson`_
	focuson was written by `Collin Greene`_ of Uber, similar to PyT it uses the `ast module`_ but unlike PyT it tracks dataflow using path-insensitive backwards slicing. Path explosion is not a problem because it is path-insensitive, but that causes it to have more false-positives than PyT.

* `PyExZ3`_
	A dynamic symbolic execution framework for Python, useful in taint tracking if it can `solve string constraints`_, which there is experimental support for in a `fork`_. 

* `DARLAB Work`_
	Has great `alias analysis work`_, by `Michael Gorbovitski`_ et al. It would be quite performance intensive to add to a security tool and may or may not be helpful for reducing false positives, but is quite impressive work regardless.

* `RIPS`_ for PHP
	The latest versions, the useful ones, are closed-source, as the author has gone commercial. This is unfortunate and it seems like the most advanced tool in this category as far as we know because it can find `second order`_ vulnerabilities. The old unsophisticated open-source version is `here`_.

* `Brakeman`_ for Rails
	Brakeman was written by `Justin Collins`_, it is written in Ruby and made for Rails.

* `Joseph Near`_ et al. for Rails
	Joseph has a lot of interesting work I would like to summarize.

.. _Bandit: https://github.com/openstack/bandit

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
.. _here: https://github.com/robocoder/rips-scanner
.. _second order: https://www.usenix.org/system/files/conference/usenixsecurity14/sec14-paper-dahse.pdf

.. _Brakeman: https://github.com/presidentbeef/brakeman
.. _Justin Collins: https://twitter.com/presidentbeef

.. _Joseph Near: http://people.eecs.berkeley.edu/~jnear/


Related Papers
==========================================

* `Alias Analysis for Optimization of Dynamic Languages`_

* `Static Detection of Second Order Vulnerabilities in Web Applications`_

* `Finding Security Bugs in Web Applications using a Catalog of Access Control Patterns`

* `Derailer Interactive Security Analysis for Web Applications`_

.. _Alias Analysis for Optimization of Dynamic Languages: http://www3.cs.stonybrook.edu/~liu/papers/Alias-DLS10.pdf
.. _Static Detection of Second Order Vulnerabilities in Web Applications: https://www.usenix.org/system/files/conference/usenixsecurity14/sec14-paper-dahse.pdf
.. _Derailer Interactive Security Analysis for Web Applications: http://people.eecs.berkeley.edu/~jnear/papers/ase14.pdf

