import pytest
import droot

@pytest.mark.skip()
def test_digital_root():
    assert droot.digital_root(16) == 7

@pytest.mark.skip()
def test_digital_root_ten_to_one():
    assert droot.digital_root(493192) == 1
