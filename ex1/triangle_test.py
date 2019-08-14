import triangle
from inspect import cleandoc


def test_triangle_draw_large():
    expected = """
        *
        * *
        * * *
        * * * *
        * * * * *"""
    assert cleandoc(expected) == triangle.draw(n=5)


def test_triangle_draw_small():
    expected = """
        *
        * *"""
    assert cleandoc(expected) == triangle.draw(n=2)
