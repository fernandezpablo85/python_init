import pytest
import desc

@pytest.mark.skip()
def test_order_cero():
    assert desc.descending_order(0) == 0

@pytest.mark.skip()
def test_order_two_numbers():
    assert desc.descending_order(15) == 51

@pytest.mark.skip()
def test_order_numbers():
    assert desc.descending_order(123456789) == 987654321