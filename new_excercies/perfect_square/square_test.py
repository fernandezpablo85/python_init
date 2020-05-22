import pytest
import square

@pytest.mark.skip
def test_is_square_negative():
    assert square.is_square(-1) == False

@pytest.mark.skip
def test_is_square_cero():
    assert square.is_square(0) == True

@pytest.mark.skip
def test_is_not_square():
    assert square.is_square(3) == False

@pytest.mark.skip
def test_is_square():
    assert square.is_square(25) == True
