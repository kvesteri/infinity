try:
    from functools import total_ordering
except ImportError:
    # Use Python 2.6 port
    from total_ordering import total_ordering


__version__ = '1.1'


@total_ordering
class Infinity(object):
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
        return True

    def __nonzero__(self):
        return True

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

    def __abs__(self):
        return self.__class__()

    def __pos__(self):
        return self

    def __div__(self, other):
        if isinstance(other, self.__class__):
            return NotImplemented

        return Infinity(
            other > 0 and self.positive or other < 0 and not self.positive
        )

    __truediv__ = __div__

    def __mul__(self, other):
        if other is 0:
            return NotImplemented
        return Infinity(
            other > 0 and self.positive or other < 0 and not self.positive
        )

    def __pow__(self, other):
        if other is 0:
            return NotImplemented
        elif other == -self:
            return -0.0 if not self.positive else 0.0
        else:
            return Infinity()

    def __rpow__(self, other):
        if other in (1, -1):
            return NotImplemented
        elif other == -self:
            return -0.0 if not self.positive else 0.0
        else:
            return Infinity()


inf = Infinity()
