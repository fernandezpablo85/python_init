import pytest
import even_index

@pytest.mark.skip
def test_even_index():
    assert even_index.find_even_index([1,2,3,4,3,2,1]) == 3

@pytest.mark.skip
def test_even_index_not_found():
    assert even_index.find_even_index([1,2,3,4,5,6]) == -1

@pytest.mark.skip
def test_even_index_eq_num():
    assert even_index.find_even_index([20,10,30,10,10,15,35]) == 3

@pytest.mark.skip
def test_even_index_first_index():
    assert even_index.find_even_index([0,0,0,0]) == 0 #Must return the first index if more cases are valid"

@pytest.mark.skip
def test_even_index_pair():
    assert even_index.find_even_index([8,8]) == -1