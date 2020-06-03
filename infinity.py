from functools import total_ordering

__version__ = '1.5'


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
        return (
            isinstance(other, self.__class__) and
            other.positive == self.positive
        ) or (
            self.positive and other == float('inf')
        ) or (
            not self.positive and other == float('-inf')
        )

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
        if is_infinite(other) and other != self:
            return NotImplemented
        return self

    def __radd__(self, other):
        return self

    def __sub__(self, other):
        if is_infinite(other) and other == self:
            return NotImplemented
        return self

    def __rsub__(self, other):
        return self

    def timetuple(self):
        return tuple()

    def __abs__(self):
        return self.__class__()

    def __pos__(self):
        return self

    def __div__(self, other):
        if is_infinite(other):
            return NotImplemented

        return Infinity(
            other > 0 and self.positive or other < 0 and not self.positive
        )

    def __rdiv__(self, other):
        return 0

    def __repr__(self):
        return str(self)

    __truediv__ = __div__
    __rtruediv__ = __rdiv__
    __floordiv__ = __div__
    __rfloordiv__ = __rdiv__

    def __mul__(self, other):
        if other == 0:
            return NotImplemented
        return Infinity(
            other > 0 and self.positive or other < 0 and not self.positive
        )

    __rmul__ = __mul__

    def __pow__(self, other):
        if other == 0:
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

    def __hash__(self):
        return (self.__class__, self.positive).__hash__()


inf = Infinity()


def is_infinite(value):
    return value == inf or value == -inf
