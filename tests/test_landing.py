import pytest
from ..models.landing import Landing


def test_landing_init_length():
    with pytest.raises(ValueError):
        assert Landing(length="abc", width=1.2, height=3)

    with pytest.raises(ValueError):
        assert Landing(length=-1, width=1.2, height=3)

    with pytest.raises(ValueError):
        assert Landing(length=True, width=1.2, height=3)


def test_landing_init_width():
    with pytest.raises(ValueError):
        assert Landing(length=1.2, width="abc", height=3)

    with pytest.raises(ValueError):
        assert Landing(length=1.2, width=-1, height=3)

    with pytest.raises(ValueError):
        assert Landing(length=1.2, width=True, height=3)


def test_landing_init_height():
    with pytest.raises(ValueError):
        assert Landing(length=1.2, width=1.2, height="abc")

    with pytest.raises(ValueError):
        assert Landing(length=1.2, width=1.2, height=-1)

    with pytest.raises(ValueError):
        assert Landing(length=1.2, width=1.2, height=True)