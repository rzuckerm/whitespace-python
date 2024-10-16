Change Log
----------

`1.0.0`_ (2024-10-12)
+++++++++++++++++++++

**Added**

- `Black <https://black.readthedocs.io/en/stable/>`_ in order to make formatting consistent
- Add CODEOWNERS file (fixes `#8 <https://github.com/rzuckerm/whitespace-python/issues/8>`_)
- Add Github actions for the following:

  - Lint and Test (fixes `#6 <https://github.com/rzuckerm/whitespace-python/issues/6>`_)
  - Publish (fixes `#7 <https://github.com/rzuckerm/whitespace-python/issues/7>`_)

- Add tests for CLI (fixes `#14 <https://github.com/rzuckerm/whitespace-python/issues/14>`_). Test coverage is now **100%**

**Changed**

- Forked `<https://github.com/dwayne/whitespace-python>`_ to `<https//github.com/rzuckerm/whitespace-python>`_
- Renamed package from ``whitespace`` to ``whitespace2`` (fixes `#9 <https://github.com/rzuckerm/whitespace-python/issues/9>`_)
- Convert project to use `Poetry <https://python-poetry.org/docs/>`_ in order to simplify dependency management and publishing (fixes `#5 <https://github.com/rzuckerm/whitespace-python/issues/5>`_)
- Number and label parsing is now done iteratively instead of recursively (fixes `#3 <https://github.com/rzuckerm/whitespace-python/issues/3>`_)
- ``whitespace.interpreter.eval`` is renamed to ```whitespace.interpreter.run`` (fixes `#2 <https://github.com/rzuckerm/whitespace-python/issues/2>`_)

`1.0.0-beta.8`_ (2018-08-31)
++++++++++++++++++++++++++++

**Added**

- A major rewrite of the system
- A ``setup.cfg`` and simplified ``setup.py``
- `Pylint <https://pylint.readthedocs.io/en/stable/>`_ in order to keep an eye on the code style and quality

**Changed**

- Start to use `pyenv <https://github.com/pyenv/pyenv>`_ and `pipenv <https://github.com/pypa/pipenv>`_ for development
- Switch to semantic versioning

**Fixed**

- The 40! bug


`1.0.0b2`_ (2016-09-03)
+++++++++++++++++++++++

**Added**

- A change log (guided by https://keepachangelog.com/)
- Notes on installation, usage, development and testing to the README
- A version badge from https://shields.io/
- Begin tracking development dependencies

**Changed**

- Explicitly list the packages to be included in the distribution
- Stop including tests in the distribution
- Stop using ``codecs.open`` since ``open`` does the job in Python 3
- Consistently name test cases with a TestCase suffix

`1.0.0b1`_ (2016-09-02)
+++++++++++++++++++++++

**Added**

- A fully tested parser with error handling and source location tracking
- An interpreter
- A CLI for running the interpreter

**Fixed**

- Fix the console's output buffering by flushing after every write

`0.1.0.dev2`_ (2016-09-01)
++++++++++++++++++++++++++

**Changed**

- Update ``MANIFEST.in`` and ``setup.py`` to ensure the correct files are included in the distribution


`0.1.0.dev1`_ (2016-08-31)
++++++++++++++++++++++++++

**Added**

- A virtual machine
- A console abstraction to make it easier to test I/O
- The stack manipulation, arithmetic, heap access, flow control and I/O instructions

0.0.1.dev1 (2016-08-31)
+++++++++++++++++++++++

Birth!

.. _`Unreleased`: https://github.com/rzuckerm/whitespace-python/compare/v1.0.0...HEAD
.. _`1.0.0`: https://github.com/rzuckerm/whitespace-python/compare/v1.0.0-beta.8...v1.0.0
.. _`1.0.0-beta.8`: https://github.com/dwayne/whitespace-python/compare/v1.0.0b2...v1.0.0-beta.8
.. _`1.0.0b2`: https://github.com/dwayne/whitespace-python/compare/v1.0.0b1...v1.0.0b2
.. _`1.0.0b1`: https://github.com/dwayne/whitespace-python/compare/v0.1.0.dev2...v1.0.0b1
.. _`0.1.0.dev2`: https://github.com/dwayne/whitespace-python/compare/v0.1.0.dev1...v0.1.0.dev2
.. _`0.1.0.dev1`: https://github.com/dwayne/whitespace-python/compare/v0.0.1.dev1...v0.1.0.dev1
