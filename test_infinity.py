from datetime import datetime
import pytest
import six
from infinity import inf, Infinity


class TestNegativeInfinity(object):
    def test_boolean_coercion(self):
        assert bool(-inf) is True

    def test_unicode_coercion(self):
        assert six.text_type(-inf) == '-inf'

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
        assert not (-inf != -inf)
        assert -inf == -Infinity()
        assert not (-inf != -Infinity())

    def test_sub_operator(self):
        assert -inf - inf == -inf

    def test_add_operator(self):
        with pytest.raises(TypeError):
            assert -inf + inf

    def test_abs(self):
        assert abs(-inf) == inf

    def test_pos(self):
        assert +-inf == -inf

    def test_div(self):
        with pytest.raises(TypeError):
            -inf / -inf
        assert (-inf / 2) == -inf
        assert (-inf / -1) == inf

    def test_mul(self):
        with pytest.raises(TypeError):
            -inf * 0
        -inf * 3 == -inf
        -inf * inf == -inf

    def test_pow(self):
        with pytest.raises(TypeError):
            pow(-inf, 0)
        pow(-inf, 3) == -inf
        pow(-inf, inf) == inf
        pow(-inf, -inf) == -0.0
        pow(-inf, -3) == -0.0

    def test_rpow(self):
        with pytest.raises(TypeError):
            pow(1, inf)
        with pytest.raises(TypeError):
            pow(-1, inf)
        pow(2, inf) == inf
        pow(-3, inf) == inf


class TestInfinity(object):
    def test_boolean_coercion(self):
        assert bool(inf) is True

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
        assert not (inf != inf)
        assert inf == Infinity()
        assert not (inf != Infinity())

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

    def test_div(self):
        with pytest.raises(TypeError):
            assert inf / inf
        assert inf / 2 == inf
        assert inf / -1 == -inf

    def test_pow(self):
        with pytest.raises(TypeError):
            pow(inf, 0)
        pow(inf, 3) == -inf
        pow(inf, inf) == inf
        pow(inf, -inf) == 0.0
        pow(inf, -3) == 0.0

    def test_rpow(self):
        with pytest.raises(TypeError):
            pow(1, inf)
        with pytest.raises(TypeError):
            pow(-1, inf)
        pow(2, inf) == inf
        pow(-3, inf) == inf
