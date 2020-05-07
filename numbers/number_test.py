# from .numbers import add
import pytest
import number


def test_sum_two_numbers():
    assert number.add(1, 2) == 3


@pytest.mark.skip()
def test_is_even():
    assert number.is_even(2)
    assert number.is_even(0)
    assert not number.is_even(1)
    assert not number.is_even(123421)


@pytest.mark.skip()
def test_is_odd():
    assert not number.is_odd(0)
    assert number.is_odd(1)
    assert not number.is_odd(2222)


@pytest.mark.skip()
def test_is_prime():
    assert number.is_prime(2)
    assert number.is_prime(7)
    assert number.is_prime(11)
    assert not number.is_prime(10)
    assert not number.is_prime(9)


@pytest.mark.skip()
def test_sum_all_array():
    assert number.sum_all([1, 2, 3, 4]) == 10
    assert number.sum_all([1]) == 1
    assert number.sum_all([1, 1, -1, -1]) == 0


@pytest.mark.skip()
def test_sum_all_array_varags():
    assert number.sum_all(1, 2, 3, 4) == 10
    assert number.sum_all(1) == 1
    assert number.sum_all(1, 1, -1, -1) == 0


@pytest.mark.skip()
def test_most_popular():
    assert number.most_popular([1]) == 1
    assert number.most_popular([1, 2]) == 1
    assert number.most_popular([1, 1, 3, 3, 3, 4, 4, 4]) == 3
