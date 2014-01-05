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
