Past Evaluations
==========================


November 16-17th, 2017
--------------------------------------

So back in the day `Bruno`_ had made a `large CSV file`_ of open-source Flask repositories, 547 unique ones to be exact, 66 had problems downloading (maybe removed between now and then) so I cloned 481 unique open-source repos. [#]_

I decided, to stay focused during the hackathon, and complete my goal in time, that I would only look for open-redirects. Open-redirects are when you can send somebody a link like ``https://chase.com?next=http://evil.com`` or ``https://chase.com?next=%68%74%74%70%73%3a%2f%2f%77%77%77%2e%65%76%69%6c%2e%63%6f%6d`` and evil.com has a phishing page on it. The reason I chose open-redirects as my one bug class is because in my experience, there are less secondary nodes involved. e.g.

.. code-block:: python

		@app.route('/login/authorized')
		@facebook.authorized_handler
		def facebook_authorized(resp):
		    next_url = request.args.get('next') or url_for('new_paste')
		    if resp is None:
		        flash('You denied the login')
		        return redirect(next_url)
		    # ...

By 'secondary nodes', I mean the arg typically is retrieved and then placed in ``redirect()``, it isn't passed into another function, or used in an assignment somewhere else. This makes them somewhat easier to find statically, as there are less things that can go wrong.


In order to evaluate the tool, I needed to know which repositories actually had vulnerabilities in them, so I put my `junk hacking`_ skills to work and made 2 regular expressions. ``".*redirect\([a-zA-Z0-9_]+\).*"`` and ``".*redirect\(request.*\).*"``. The first one detects any redirect call with a variable as the only argument, and the second detects any redirect call with request.anything as the first argument. These aren't perfect, but have a good chance of detecting 90 something percent of possibly vulnerable calls. (The CSV file somehow had a controller file associated with each repo, and each regex was run on every line.)

This narrowed it down to 20 repositories, around ~4.1 percent. 17 repos matched the first regex, and 3 matched the second. [#]_

The great: 4 true positives were reported, although 3 of them are in ``@twitter.authorized_handler`` or ``@facebook.authorized_handler`` controllers (used in OAuth.) The only notable one is noted first, as it is in code written by the creator of Flask.

	* `mitsuhiko/flask-pastebin`_ 5 vulns reported, 1, 2, 3: really false: reported as unknown (GitHub issues incoming, but partially due to us `not checking the "Does this return a tainted value with tainted args?" mapping`_ for ``url_for``) 4,5: true: true
	* `ashleymcnamara/social_project_flask`_ 2 vulns: really true, reported as true
	* `fubuki/python-bookmark-service`_ 1 vuln: really true, reported as true
	* `GandalfTheGandalf/twitter`_ 2 vulns: really true, reported as true

The good: 7 didn't have any vulnerabilities, and we didn't report any.

	* `gene1wood/flaskoktaapp`_
	* `lepture/flask-oauthlib`_
	* `sijinjoseph/multunus-puzzle`_
	* `AuthentiqID/examples-flask`_
	* `honestappalachia/honest_site`_
	* `jpf/okta-pysaml2-example`_
	* `ciaron/pandaflask_old`_

The bad: 4 had no real vulnerabilities, but had one or two false positives.

	* `billyfung/flask_shortener`_ 2 false positives (Lazy mistake of making ``.get`` a source instead of ``request.args.get`` etc., so ``redis.get`` was used as a source.)

	* `ZAGJAB/Flask_OAuth2`_ 1 false positive (Customization is needed for open-redirects, to eliminate all false-positives, because if something tainted is used in string formatting, it typically needs to be at the very beginning of the string to be a vulnerability.)

	* `amehta/Flaskly`_ 1 false positive (GitHub issue incoming.)

	* `mskog/cheapskate`_ 1 false positive (GitHub issue incoming.)

The ugly: 2 had one false-negative.

	* `oakie/oauth-flask-template`_ (GitHub issue incoming.)
	* `cyberved/simple-web-proxy`_ (GitHub issue incoming.)

The fatal: 3 crashed PyT, but by sheer luck, didn't have any open-redirect vulnerabilities in them, I looked. 2 or 3 of them were caused by a `PR`_ I merged last weekend.

	* `commandknight/cs125-fooddy-flask`_ (GitHub issue incoming.)
	* `bear/python-indieweb`_ (GitHub issue incoming.)
	* `ubbochum/hb2_flask`_ (GitHub issue incoming.)

In closing, these results seem okay to me, because once the GitHub issues are made for these issues and fixed we'll be in a great place. This evaluation certainly didn't find all the bugs, but probably most of them. The next time I evaluate the tool, I think I'll look for command injection vulnerabilities or SSRF. I think the only takeaway is that for evaluating a tool like this you should use regexes to narrow down what you spend your time analyzing. I'll make a PR in the PyT repo to show what I customized to just find open-redirects, but it was mostly trimming down the `sink list`_ to just ``redirect`` and removing ``form`` from the `source list`_.


Around or before May 2016
--------------------------------------

During the writing of the `original thesis`_ PyT was run on 6 or 7 open-source projects and no vulnerabilities were found.
I think the sample size was too small.

.. [#] There are some commits in the CSV file that removed a few repos that caused issues before, but those commits were made long ago, just wanted to note the stats aren't 100% impartial.

.. [#] This isn't exactly true, if something matched the 2nd regex I removed ``".*redirect\(request\.url\).*"`` and ``".*redirect\(request\.referrer\).*"``.

.. _Bruno: https://github.com/Thalmann
.. _large CSV file: https://github.com/python-security/pyt/blob/master/flask_open_source_apps.csv
.. _junk hacking: https://lists.immunityinc.com/pipermail/dailydave/2014-September/000746.html
.. _not checking the "Does this return a tainted value with tainted args?" mapping: https://github.com/python-security/pyt/blob/master/pyt/base_cfg.py#L829
.. _original thesis: http://projekter.aau.dk/projekter/files/239563289/final.pdf#page=83
.. _source list: https://github.com/python-security/pyt/blob/master/pyt/trigger_definitions/flask_trigger_words.pyt#L4-L5
.. _sink list: https://github.com/python-security/pyt/blob/master/pyt/trigger_definitions/flask_trigger_words.pyt#L20

.. _mitsuhiko/flask-pastebin: https://github.com/mitsuhiko/flask-pastebin/blob/master/pastebin.py#L140-L159
.. _ashleymcnamara/social_project_flask: https://github.com/ashleymcnamara/social_project_flask/blob/master/app.py#L36-L48
.. _fubuki/python-bookmark-service: https://github.com/fubuki/python-bookmark-service/blob/master/app.py#L62
.. _GandalfTheGandalf/twitter: https://github.com/GandalfTheGandalf/twitter/blob/master/hello.py#L160-L178
.. _gene1wood/flaskoktaapp: https://github.com/gene1wood/flaskoktaapp/blob/master/flaskoktaapp/__init__.py#L204

.. _lepture/flask-oauthlib: https://github.com/lepture/flask-oauthlib/blob/master/flask_oauthlib/provider/oauth1.py
.. _sijinjoseph/multunus-puzzle: https://github.com/sijinjoseph/multunus-puzzle/blob/master/src/app.py
.. _AuthentiqID/examples-flask: https://github.com/AuthentiqID/examples-flask/blob/master/example_basic.py
.. _honestappalachia/honest_site: https://github.com/honestappalachia/honest_site/blob/master/run.py
.. _jpf/okta-pysaml2-example: https://github.com/jpf/okta-pysaml2-example/blob/master/app.py#L181-L222
.. _ciaron/pandaflask_old: https://github.com/ciaron/pandaflask_old/blob/master/pandachrome.py

.. _billyfung/flask_shortener: https://github.com/billyfung/flask_shortener/blob/master/app.py#L56
.. _ZAGJAB/Flask_OAuth2: https://github.com/ZAGJAB/Flask_OAuth2/blob/master/app.py#L75-L77
.. _amehta/Flaskly: https://github.com/amehta/Flaskly/blob/master/flaskly.py#L65
.. _mskog/cheapskate: https://github.com/mskog/cheapskate/blob/master/cheapskate.py#L55

.. _oakie/oauth-flask-template: https://github.com/oakie/oauth-flask-template/blob/master/auth.py#L63
.. _cyberved/simple-web-proxy: https://github.com/cyberved/simple-web-proxy/blob/master/app.py#L73

.. _PR: https://github.com/python-security/pyt/pull/63
.. _commandknight/cs125-fooddy-flask: https://github.com/commandknight/cs125-fooddy-flask/blob/master/fooddy2.py
.. _bear/python-indieweb: https://github.com/bear/python-indieweb/blob/master/indieweb.py
.. _ubbochum/hb2_flask: https://github.com/ubbochum/hb2_flask/blob/master/hb2_flask.py
