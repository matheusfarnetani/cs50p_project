import pytest
from ..models.accessible_ramp import AccessibleRamp


def test_accessible_ramp_init_height():
    with pytest.raises(ValueError):
        assert AccessibleRamp(height="abc", width=1.2, option="COM-C", slope=8.33)

    with pytest.raises(ValueError):
        assert AccessibleRamp(height=-1, width=1.2, option="COM-C", slope=8.33)

    with pytest.raises(ValueError):
        assert AccessibleRamp(height=True, width=1.2, option="COM-C", slope=8.33)


def test_accessible_ramp_init_width():
    with pytest.raises(ValueError):
        assert AccessibleRamp(height=3, width="abc", option="COM-C", slope=8.33)

    with pytest.raises(ValueError):
        assert AccessibleRamp(height=3, width=-1, option="COM-C", slope=8.33)

    with pytest.raises(ValueError):
        assert AccessibleRamp(height=3, width=True, option="COM-C", slope=8.33)


def test_accessible_ramp_init_option():
    with pytest.raises(ValueError):
        assert AccessibleRamp(height=3, width=1.2, option=2, slope=8.33)

    with pytest.raises(ValueError):
        assert AccessibleRamp(height=3, width=1.2, option="abc", slope=8.33)

    with pytest.raises(ValueError):
        assert AccessibleRamp(height=3, width=1.2, option=True, slope=8.33)


def test_accessible_ramp_init_slope():
    with pytest.raises(ValueError):
        assert AccessibleRamp(height=3, width=1.2, option="COM-C", slope="abc")

    with pytest.raises(ValueError):
        assert AccessibleRamp(height=3, width=1.2, option="COM-C", slope=12.6)

    with pytest.raises(ValueError):
        assert AccessibleRamp(height=3, width=1.2, option="COM-C", slope=-8.33)

    with pytest.raises(ValueError):
        assert AccessibleRamp(height=3, width=1.2, option="COM-C", slope=True)
