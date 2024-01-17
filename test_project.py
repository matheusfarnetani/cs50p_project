from .project import max_possible_height, max_possible_slope, get_float


def test_max_possible_height():
    assert len(max_possible_height(8.33, 1, .5)) == 22
    assert max_possible_height(8.33, 1, .5)[-1].height == 11.5


def test_max_possible_slope():
    ...


def get_float():
    ...