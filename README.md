infinity
========

All-in-one infinity value for Python. Can be compared to any object.


Supports rich comparison methods:


```python

from infinity import inf
import sys

3 < inf                     # True
datetime(2000, 2, 2) < inf  # True
-inf < inf                  # True
inf == inf                  # True
-inf == -inf                # True
```


Also supports arithmetic operators:

```python
inf + inf                   # inf
-inf - inf                  # -inf

inf + 3                     # inf
inf + datetime(2000, 2, 2)  # inf

inf / inf                   # 0.0
inf / -inf                  # -0.0
```

The following operations raise `TypeError`s:

```python
inf - inf
-inf + inf
inf / inf
inf * 0
pow(inf, 0)
```

Infinity can be coerced to various types:

```python

float(inf)          # float('inf')
float(-inf)         # float('-inf')
str(inf)            # 'inf'
str(-inf)           # '-inf'
bool(inf)           # True
bool(-inf)          # False
```
