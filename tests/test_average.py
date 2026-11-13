
from test_cillm import average


def test_average_normal():
    assert average([2, 4, 6]) == 4


def test_average_empty():
    assert average([]) == 0
