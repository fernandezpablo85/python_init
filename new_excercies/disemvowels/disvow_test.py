import disvow
import pytest

@pytest.mark.skip()
def test_disvowel():
    assert disvow.disemvowel("This website is for losers LOL!") == "Ths wbst s fr lsrs LL!"
