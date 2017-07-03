.. _contributing-to-pyt:

Contributing
=============================

You are here to help on PyT? Awesome, feel welcome and read the
following sections in order to know what and how to work on something. If you
get stuck at any point you can create a `ticket on GitHub`_.

Join our slack group: https://pyt-dev.slack.com/ - to ask for an invite, email mr.thalmann@gmail.com

Please make sure you are welcoming and friendly in all of our spaces.

.. _ticket on GitHub: https://github.com/python-security/pyt/issues

Contributing to development
---------------------------

If you want to deep dive and help out with development on PyT, then
first set up a development environement according to the
:ref:`virtual env setup guide <install>`. After that is done we
suggest you have a look at tickets in our issue tracker that are labelled `Easy`_.
These are meant to be a great way to get a smooth start and
won't put you in front of the most complex parts of the system.

Procedure for adding new features:

* Pitch idea in slack
* Create issue in Github
* Develop the feature in a separate feature-branch
  * Feature branch names should start with the issues number and is allowed to contain letters and underscores, for instance: 12_add_new_awesome_feature
  * Remember to write unit tests and docstrings for your code, and if necessary documentation
* Announce finished feature as pull request
* Pull request reviewed by at least 1
* Merge to development branch when ready
* Merge into master when we all agree


.. _Easy: https://github.com/python-security/pyt/issues?q=is%3Aopen+is%3Aissue+label%3Aeasy
