import pytest
from ..models.ramp import Ramp


def test_Ramp_init_height():
    with pytest.raises(ValueError):
        assert Ramp(height="abc", width=1.2, slope=8.33)

    with pytest.raises(ValueError):
        assert Ramp(height=-1, width=1.2, slope=8.33)

    with pytest.raises(ValueError):
        assert Ramp(height=True, width=1.2, slope=8.33)


def test_Ramp_init_width():
    with pytest.raises(ValueError):
        assert Ramp(height=3, width="abc", slope=8.33)

    with pytest.raises(ValueError):
        assert Ramp(height=3, width=-1, slope=8.33)

    with pytest.raises(ValueError):
        assert Ramp(height=3, width=True, slope=8.33)


def test_Ramp_init_length():
    with pytest.raises(ValueError):
        assert Ramp(height=3, width=1.2, length="abc")

    with pytest.raises(ValueError):
        assert Ramp(height=3, width=1.2, length=-1)

    with pytest.raises(ValueError):
        assert Ramp(height=3, width=1.2, length=True)


def test_Ramp_init_slope():
    with pytest.raises(ValueError):
        assert Ramp(height=3, width=1.2, slope="abc")

    with pytest.raises(ValueError):
        assert Ramp(height=3, width=1.2, slope=-1)

    with pytest.raises(ValueError):
        assert Ramp(height=3, width=1.2, slope=True)
