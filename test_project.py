from .project import max_possible_height, max_possible_slope, other_options


def test_max_possible_height():
    assert len(max_possible_height(8.33, 1, .5)) == 22
    assert max_possible_height(8.33, 1, .5)[-1].height == 11.5


def test_max_possible_slope():
    assert len(max_possible_slope(3, 5, 0.2)) == 17
    assert max_possible_slope(3, 5, 0.2)[-1].slope == 8.200000000000001


def test_other_options():
    assert len(other_options(3, 1.2)) == 3
    assert len(other_options(.5, 1.2)) == 4
    assert len(other_options("abc", 1.2)) == 0
    assert len(other_options(3, "abc")) == 0