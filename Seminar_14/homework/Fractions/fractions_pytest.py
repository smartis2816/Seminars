import pytest
from fractions_doctest import sum_fractions, mult_fractions


def test_sum_fractions():
    assert sum_fractions(3, 4, 7, 8) == '13/8'


def test_mult_fractions():
    assert mult_fractions(3, 4, 7, 8) == '21/32'


if __name__ == '__main__':
    pytest.main(['-v'])
