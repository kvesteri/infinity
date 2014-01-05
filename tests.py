import pytest
from infinity import inf, Infinity


@pytest.mark.parametrize('value', [
    None,
    '',
    12,
    -inf,
])
def test_infinity_is_greater_than_every_other_value(value):
    assert value < inf
    assert inf > value


def test_infinity_is_not_greater_than_itself():
    assert not (inf < inf)


def test_other_comparison_methods_for_infinity():
    assert inf <= inf
    assert inf == inf
    assert not (inf != inf)
    assert inf == Infinity()
    assert not (inf != Infinity())


@pytest.mark.parametrize('value', [
    None,
    '',
    12,
    inf,
])
def test_negative_infinity_is_smaller_than_every_other_value(value):
    assert value > -inf


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


class TestInfinity(object):
    def test_boolean_coercion(self):
        assert bool(inf) is True

    def test_string_coercion(self):
        assert str(inf) == 'inf'

    def test_unicode_coercion(self):
        assert unicode(inf) == 'inf'


