from datetime import datetime
import pytest
from infinity import inf, Infinity


def test_infinity_is_not_greater_than_itself():
    assert not (inf < inf)


def test_other_comparison_methods_for_infinity():
    assert inf <= inf
    assert inf == inf
    assert not (inf != inf)
    assert inf == Infinity()
    assert not (inf != Infinity())


def test_min_is_not_greater_than_itself():
    assert not (-inf < -inf)


def test_other_comparison_methods_for_negative_infinity():
    assert -inf <= -inf
    assert -inf == -inf
    assert not (-inf != -inf)
    assert -inf == -Infinity()
    assert not (-inf != -Infinity())


class TestNegativeInfinity(object):
    def test_boolean_coercion(self):
        assert bool(-inf) is False

    def test_string_coercion(self):
        assert str(-inf) == '-inf'

    def test_unicode_coercion(self):
        assert unicode(-inf) == '-inf'

    def test_float_coercion(self):
        assert float(-inf) == float('-inf')

    @pytest.mark.parametrize('value', [
        None,
        '',
        12,
        inf,
        datetime(2000, 2, 2)
    ])
    def test_smaller_than_every_other_value(self, value):
        assert value > -inf
        assert -inf < value

    def test_sub_operator(self):
        assert -inf - inf == -inf

    def test_add_operator(self):
        with pytest.raises(TypeError):
            assert -inf + inf

    def test_abs(self):
        assert abs(-inf) == inf

    def test_pos(self):
        assert +-inf == -inf


class TestInfinity(object):
    def test_boolean_coercion(self):
        assert bool(inf) is True

    def test_string_coercion(self):
        assert str(inf) == 'inf'

    def test_unicode_coercion(self):
        assert unicode(inf) == 'inf'

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

    def test_add_operator(self):
        assert inf + inf == inf
        assert inf + 3 == inf
        assert inf + datetime(2000, 2, 2) == inf

    def test_sub_operator(self):
        with pytest.raises(TypeError):
            inf - inf

    def test_abs(self):
        assert abs(inf) == inf

    def test_pos(self):
        assert +inf == inf
