Frequently Asked Questions
==========================

Why do you not support Python2?
--------------------------------------

It's on our near-term roadmap, we're currently trying to iron-out our Python3 support before giving our full attention to Python 2 support.

How do you deal with path explosion?
--------------------------------------
Because of the way reaching definitions unions predecessors we don't explode for the entire program we're analysing, just during conditionals i.e. after an if statement is done we're back with dealing with one path.

Do you do inlining or summaries for inter-procedural analysis?
--------------------------------------

Inlining, but a long-term goal is to re-write PyT to use summaries instead so that we can e.g. analyze a PR and only spend time analysing the difference. This is probably the last thing on our roadmap.

