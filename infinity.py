try:
    from functools import total_ordering
except ImportError:
    # Use Python 2.6 port
    from total_ordering import total_ordering


@total_ordering
class Infinity(object):
    """
    An object that is greater than any other object (except itself).

    Inspired by https://pypi.python.org/pypi/Extremes

    Examples::

    Infinity can be compared to any object:

        >>> from infinity import inf
        >>> import sys

        >>> inf > -sys.maxint
        True
        >>> inf > None
        True
        >>> inf > ''
        True
        >>> inf > datetime(2000, 20, 2)
    """
    def __init__(self, positive=True):
        self.positive = positive

    def __neg__(self):
        return Infinity(not self.positive)

    def __gt__(self, other):
        if self == other:
            return False
        return self.positive

    def __eq__(self, other):
        if (
            isinstance(other, self.__class__) and
            other.positive == self.positive
        ):
            return True
        return False

    def __ne__(self, other):
        return not (self == other)

    def __bool__(self):
        return self.positive

    def __nonzero__(self):
        return self.positive

    def __str__(self):
        return '%sinf' % ('' if self.positive else '-')

    def __float__(self):
        return float(str(self))

    def __add__(self, other):
        if (
            isinstance(other, self.__class__) and
            other.positive != self.positive
        ):
            return NotImplemented
        return self

    def __sub__(self, other):
        if (
            isinstance(other, self.__class__) and
            other.positive == self.positive
        ):
            return NotImplemented
        return self

    def timetuple(self):
        return tuple()


inf = Infinity()
