infinity
========

All-in-one infinity value for Python. Can be compared to any object.


Why?
----

* Python has `float('inf')` and `float('-inf')`. However these simply represent
floating point infinity values. I wanted to create a class which can be compared to any comparable object.
* Writing `float('inf')` is clumsy compared to just `inf`
* `pow(1, float('inf'))` returns 1 whereas it should be undefined (see why: http://math.stackexchange.com/questions/319764/1-to-the-power-of-infinity-why-is-it-indeterminate). In infinity this operation returns TypeError.
* http://stackoverflow.com/questions/382603/when-would-you-use-infinity


Installation
------------


Simply grab the package from pypi:


    pip install infinity


Supported python versions:

* Python 2.6
* Python 2.7
* Python 3.3
* PyPy


Object comparison
-----------------

The `Infinity` class supports rich comparison methods:


```python

from infinity import inf
import sys

3 < inf                     # True
datetime(2000, 2, 2) < inf  # True
-inf < inf                  # True
inf == inf                  # True
-inf == -inf                # True
```

Arithmetic operators
--------------------


It also supports arithmetic operators:

```python
inf + inf                   # inf
-inf - inf                  # -inf

inf + 3                     # inf
inf + datetime(2000, 2, 2)  # inf

5 / inf                     # 0.0
3 / -inf                    # -0.0

pow(inf, 0.5)               #
```

The following operations raise `TypeError` exceptions:

```python
inf - inf
-inf + inf
inf / inf
inf * 0
pow(inf, 0)
pow(1, inf)
```

Type coercion
-------------

Infinity objects can be coerced to various types:

```python

float(inf)          # float('inf')
float(-inf)         # float('-inf')
str(inf)            # 'inf'
str(-inf)           # '-inf'
bool(inf)           # True
bool(-inf)          # True
```
