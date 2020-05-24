import triangle
from inspect import cleandoc
import pytest

""" Hice una funcion en triangle.py, que logra la imagen, pero no entiendo como pasarsela a estas funciones """ 

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
