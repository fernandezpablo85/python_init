import dist
import pytest
import math



def test_mean_distance():
    p1, p2, p3 = (0, 0), (2, 0), (2, 2)
    expected = math.sqrt(8)
    actual = dist.mean_distance(p1, p2, p3)
    assert math.isclose(expected, actual)
