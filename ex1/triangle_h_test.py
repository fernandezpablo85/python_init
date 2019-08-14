import triangle

from hypothesis import given, strategies as st


@given(st.integers(min_value=1, max_value=100))
def test_triangle_characters(n):
    t = triangle.draw(n=n)

    newlines = n - 1
    stars = n * (n + 1) / 2
    assert t.count("\n") == newlines
    assert t.count("*") == stars

    lines = t.split("\n")
    if len(lines) >= 2:
        mid = n // 2
        assert len(lines[mid]) == len(lines[mid - 1]) + 2

