import pytest
import find_odd

@pytest.mark.skip()
def test_find_it_positive():
    assert find_odd.find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]) == 5

@pytest.mark.skip()
def test_find_it_negative():
    assert find_odd.find_it([1,1,2,-2,5,2,4,4,-1,-2,5]) == -1

@pytest.mark.skip()
def test_find_it_one_num():
    assert find_odd.find_it([10]) == 10

@pytest.mark.skip()
def test_find_it_one_rep():
    assert find_odd.find_it([5,4,3,2,1,5,4,3,2,10,10]) == 1
