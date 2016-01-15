infinity
========

|Build Status| |Version Status| |Downloads|

All-in-one infinity value for Python. Can be compared to any object.


Why?
----

* Python has ``float('inf')`` and ``float('-inf')``. However these simply
  represent floating point infinity values. I wanted to create a class which can
  be compared to any comparable object.

* Writing ``float('inf')`` is clumsy compared to just ``inf``

* ``pow(1, float('inf'))`` returns 1 whereas `it should be undefined`_. In
  infinity this operation returns ``TypeError``.

* `When would you use Infinity`_?

.. _it should be undefined:
   http://math.stackexchange.com/questions/319764
   /1-to-the-power-of-infinity-why-is-it-indeterminate

.. _When would you use Infinity:
   http://stackoverflow.com/questions/382603/when-would-you-use-infinity

Installation
------------


Simply grab the package from pypi::


    pip install infinity


Supported python versions:

* Python 2.6
* Python 2.7
* Python 3.3
* Python 3.4
* Python 3.5
* PyPy


Object comparison
-----------------

The ``Infinity`` class supports rich comparison methods:


.. code-block:: python

    >>> import sys
    >>> from datetime import datetime
    >>> from infinity import inf

    >>> 3 < inf
    True
    >>> datetime(2000, 2, 2) < inf
    True
    >>> -inf < inf
    True
    >>> inf == inf
    True
    >>> -inf == -inf
    True


Arithmetic operators
--------------------


It also supports arithmetic operators:

.. code-block:: python

    >>> inf + inf
    inf
    >>> -inf - inf
    -inf

    >>> inf + 3
    inf
    >>> inf + datetime(2000, 2, 2)
    inf

    >>> 5 / inf
    0
    >>> 3 / -inf
    0
    >>> pow(inf, 0.5)
    inf

The following operations raise ``TypeError`` exceptions:

.. code-block:: python

    >>> inf - inf
    Traceback (most recent call last):
        ...
    TypeError: unsupported operand type(s) for -: 'Infinity' and 'Infinity'

    >>> -inf + inf
    Traceback (most recent call last):
        ...
    TypeError: unsupported operand type(s) for +: 'Infinity' and 'Infinity'

    >>> inf / inf  # doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
        ...
    TypeError: unsupported operand type(s) for /: 'Infinity' and 'Infinity'

    >>> inf * 0
    Traceback (most recent call last):
        ...
    TypeError: unsupported operand type(s) for *: 'Infinity' and 'int'

    >>> pow(inf, 0)  # doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
        ...
    TypeError: unsupported operand type(s) for ** or pow(): 'Infinity' and 'int'

    >>> pow(1, inf)  # doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
        ...
    TypeError: unsupported operand type(s) for ** or pow(): 'int' and 'Infinity'


Type coercion
-------------

Infinity objects can be coerced to various types:


.. code-block:: python

    >>> float(inf) == float('inf')
    True
    >>> float(-inf) == float('-inf')
    True
    >>> str(inf)
    'inf'
    >>> str(-inf)
    '-inf'
    >>> bool(inf)
    True
    >>> bool(-inf)
    True


.. |Build Status| image:: https://travis-ci.org/kvesteri/infinity.png?branch=master
   :target: https://travis-ci.org/kvesteri/infinity
.. |Version Status| image:: https://img.shields.io/pypi/v/infinity.svg
   :target: https://pypi.python.org/pypi/infinity/
.. |Downloads| image:: https://img.shields.io/pypi/dm/infinity.svg
   :target: https://pypi.python.org/pypi/infinity/
