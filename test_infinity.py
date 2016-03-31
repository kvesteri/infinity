import operator
from datetime import datetime

import pytest
import six

from infinity import inf, Infinity


class InfinityTestCase(object):
    value = inf

    def test_boolean_coercion(self):
        assert bool(self.value) is True

    @pytest.mark.parametrize(
        ('arg', 'op'),
        (
            (inf, operator.truediv),
            (0, operator.pow),
            (0, operator.mul)
        )
    )
    def test_illegal_operations(self, arg, op):
        with pytest.raises(TypeError):
            op(self.value, arg)

    @pytest.mark.parametrize(
        ('arg', 'op'),
        (
            (1, operator.pow),
            (-1, operator.pow),
            (0, operator.mul)
        )
    )
    def test_illegal_revert_operations(self, arg, op):
        with pytest.raises(TypeError):
            op(arg, self.value)

    @pytest.mark.parametrize(
        'arg',
        (
            2,
            -3,
            3.6
        )
    )
    def test_rpow(self, arg):
        pow(arg, self.value) == inf

    def test_abs(self):
        assert abs(self.value) == inf

    def test_pos(self):
        assert +self.value == self.value


class TestNegativeInfinity(InfinityTestCase):
    value = -inf

    def test_unicode_coercion(self):
        assert six.text_type(-inf) == '-inf'

    def test_repr(self):
        assert repr(-inf) == '-inf'

    def test_float_coercion(self):
        assert float(-inf) == float('-inf')

    @pytest.mark.parametrize('value', [
        None,
        '',
        12,
        inf,
        datetime(2000, 2, 2)
    ])
    def test_less_than_every_other_value(self, value):
        assert value > -inf
        assert -inf < value

    def test_not_less_than_itself(self):
        assert not (-inf < -inf)

    def test_comparison(self):
        assert -inf <= -inf
        assert -inf == -inf
        assert -inf == float(-inf)
        assert not (-inf != -inf)
        assert -inf == -Infinity()
        assert not (-inf != -Infinity())

    def test_sub_operator(self):
        assert -inf - inf == -inf

    def test_add_operator(self):
        with pytest.raises(TypeError):
            assert -inf + inf

    def test_div(self):
        with pytest.raises(TypeError):
            -inf / -inf
        assert (-inf / 2) == -inf
        assert (-inf / -1) == inf

    def test_rdiv(self):
        assert -3 / -inf == 0.0

    def test_mul(self):
        assert -inf * 3 == -inf
        assert -inf * inf == -inf

    def test_rmul(self):
        assert 3 * -inf == -inf
        assert 3.5 * -inf == -inf
        assert -3 * -inf == inf

    def test_pow(self):
        with pytest.raises(TypeError):
            pow(-inf, 0)
        pow(-inf, 3) == -inf
        pow(-inf, inf) == inf
        pow(-inf, -inf) == -0.0
        pow(-inf, -3) == -0.0


class TestInfinity(InfinityTestCase):
    def test_unicode_coercion(self):
        assert six.text_type(inf) == 'inf'

    def test_float_coercion(self):
        assert float(inf) == float('inf')

    @pytest.mark.parametrize('value', [
        None,
        '',
        12,
        -inf,
        datetime(2000, 2, 2)
    ])
    def test_greater_than_every_other_value(self, value):
        assert value < inf
        assert inf > value

    def test_not_greater_than_itself(self):
        assert not (inf < inf)

    def test_comparison(self):
        assert inf <= inf
        assert inf == inf
        assert inf == float('inf')
        assert not (inf != inf)
        assert inf == Infinity()
        assert not (inf != Infinity())

    @pytest.mark.parametrize(
        ('value1', 'value2', 'result'),
        (
            (inf, inf, inf),
            (inf, 3, inf),
            (inf, datetime(2000, 2, 2), inf),
            (3, inf, inf),
            (-3.5, inf, inf),
        )
    )
    def test_add_operator(self, value1, value2, result):
        assert value1 + value2 == result

    @pytest.mark.parametrize(
        ('value1', 'value2', 'result'),
        (
            (-inf, inf, -inf),
            (inf, 3, inf),
            (inf, datetime(2000, 2, 2), inf),
            (3, -inf, -inf),
            (-3.5, -inf, -inf),
        )
    )
    def test_sub_operator(self, value1, value2, result):
        assert value1 - value2 == result

    def test_sub_operator_with_invalid_arg(self):
        with pytest.raises(TypeError):
            inf - inf

    def test_div(self):
        assert inf / 2 == inf
        assert inf / -1 == -inf

    def test_pow(self):
        pow(inf, 3) == -inf
        pow(inf, inf) == inf
        pow(inf, -inf) == 0.0
        pow(inf, -3) == 0.0

    def test_repr(self):
        assert repr(inf) == 'inf'

    def test_hashable(self):
        assert isinstance(inf.__hash__(), int)
        assert Infinity().__hash__() == Infinity().__hash__()
        # check against 10 other objects so random hash collisions are unlikely
        assert not all(inf.__hash__() == x.__hash__() for x in range(0, 10))
