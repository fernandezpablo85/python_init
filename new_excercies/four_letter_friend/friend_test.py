import pytest
import find_friend

@pytest.mark.skip
def test_friend():
    assert find_friend.friend(["Ryan", "Kieran", "Mark",]) == ["Ryan", "Mark"]
