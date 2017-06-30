Related Work
==========================================

* `Bandit`_
	Bandit was a tool made by a few people at OpenStack with the same purpose of PyT in mind, the main difference is that Bandit doesn't track the flow of data and PyT does.

* JunkHacker
	JunkHacker was written by Kevin Hock and had an incredibly bad design, it analyzed Python bytecode using equip and tracked taint depth-first searching through a basic block's via a bytecode interpreter heavily adopted from Byterun. It merged predecessors taint sets with 

* focuson
	focuson was written by Collin Greene of Uber, similar to PyT it uses the `ast` module but unlike PyT it tracks dataflow using backwards slicing.

* PyExZ3
	A symbolic execution framework for Python, useful in taint tracking if it can solve string constraints. 

* DARLAB Work
	Has great alias analysis work, it would be quite performance intensive to add to a security tool and may or may not be helpful for reducing false positives, but is quite impressive work regardless.

* RIPS
	The latest version that is useful is closed-source, as the author has gone commercial. This is unfortunate and it seems like the most advanced tool in this category at this point in time. 

* Brakeman
	Brakeman was written by Justin Collins, it is written in Ruby and made for Rails.

.. _Bandit: https://github.com/openstack/bandit
