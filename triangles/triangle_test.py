import triangle
from inspect import cleandoc
import pytest


@pytest.mark.skip()
def test_triangle_draw_large():
    expected = """
        *
        * *
        * * *
        * * * *
        * * * * *"""
    assert cleandoc(expected) == triangle.draw(n=5)


@pytest.mark.skip()
def test_triangle_draw_small():
    expected = """
        *
        * *"""
    assert cleandoc(expected) == triangle.draw(n=2)
