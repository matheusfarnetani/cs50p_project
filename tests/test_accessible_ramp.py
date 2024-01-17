import pytest
from ..models.accessible_ramp import AccessibleRamp
from ..models.limits import Limits


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


def test_set_variables():
    l = Limits.set_by_option("COM-C")
    ar = AccessibleRamp(height=3, width=1.2, option="COM-C", slope=8.33)

    assert ar.set_variables(height=3, width=1.2, slope=8.33, limits=l) == True
    assert ar.set_variables(height=3, width=1.2, slope=8.33, limits="abc") == False
    assert ar.set_variables(height=3, width=1.2, slope=8.33, limits=1) == False 
    assert ar.set_variables(height=3, width=1.2, slope=8.33, limits=True) == False 

    with pytest.raises(ValueError):
        assert ar.set_variables(height="abc", width=1.2, slope=8.33, limits=l)
    with pytest.raises(ValueError):
        assert ar.set_variables(height=3, width="abc", slope=8.33, limits=l)
    with pytest.raises(ValueError):
        assert ar.set_variables(height=3, width=1.2, slope="abc", limits=l)


def test_calc_num_landing():
    l = Limits.set_by_option("COM-C")
    ar = AccessibleRamp(height=3, width=1.2, option="COM-C", slope=8.33)

    assert ar.calc_num_landings(3, l.max_landing) == 3.75
    assert ar.calc_num_landings(10.0, 2) == 5
    assert ar.calc_num_landings("a", 2) == None
    assert ar.calc_num_landings("a", "b") == None
    assert ar.calc_num_landings(2, "b") == None
    assert ar.calc_num_landings(True, True) == 1 # ?
    assert ar.calc_num_landings(True, False) == None
    assert ar.calc_num_landings(False, True) == 0 # ?
    assert ar.calc_num_landings(False, False) == None


def test_calc_num_segments():
    l = Limits.set_by_option("COM-C")
    ar = AccessibleRamp(height=3, width=1.2, option="COM-C", slope=8.33)

    assert ar.calc_num_segments(0, l.max_segments) == 1
    assert ar.calc_num_segments(1, l.max_segments) == 2
    assert ar.calc_num_segments("abc", l.max_segments) == None
    assert ar.calc_num_segments(1, "abc") == None
    assert ar.calc_num_segments(True, 1) == None
    assert ar.calc_num_segments(False, 1) == 1 # ?
    assert ar.calc_num_segments(1, True) == None
    assert ar.calc_num_segments(1, False) == 2 # ?


def test_create_map():
    l = Limits.set_by_option("COM-C")
    ar = AccessibleRamp(height=3, width=1.2, option="COM-C", slope=8.33)

    assert len(ar.create_map(ar.segments, ar.num_landings, l.max_landing, ar.height, ar.width, ar.slope)) == 7
    assert ar.create_map("abc", ar.num_landings, l.max_landing, ar.height, ar.width, ar.slope) == None
    assert ar.create_map(ar.segments, "abc", l.max_landing, ar.height, ar.width, ar.slope) == None
    assert ar.create_map(ar.segments, ar.num_landings, "abc", ar.height, ar.width, ar.slope) == None
    assert ar.create_map(1, 0, 15, "abc",1, 5) == None # Heights is only used when there is one segment
    assert ar.create_map(ar.segments, ar.num_landings, l.max_landing, ar.height, "abc", ar.slope) == None
    assert ar.create_map(ar.segments, ar.num_landings, l.max_landing, ar.height, -1, ar.slope) == None
    assert ar.create_map(ar.segments, ar.num_landings, l.max_landing, ar.height, ar.width, "abc") == None
    assert ar.create_map(ar.segments, ar.num_landings, l.max_landing, ar.height, ar.width, -1) == None


def test_calculate_length():
    l = Limits.set_by_option("COM-C")
    ar = AccessibleRamp(height=3, width=1.2, option="COM-C", slope=8.33)

    assert ar.calculate_length(ar.map) == ar.length
    assert ar.calculate_length("abc") == None
    assert ar.calculate_length(1) == None
    assert ar.calculate_length(-1) == None
    assert ar.calculate_length([1,1]) == None
    assert ar.calculate_length(["abc","abc"]) == None
    assert ar.calculate_length([True,True]) == None
    assert ar.calculate_length(True) == None
    assert ar.calculate_length(False) == None


def test_calculate_volume():
    l = Limits.set_by_option("COM-C")
    ar = AccessibleRamp(height=3, width=1.2, option="COM-C", slope=8.33)

    assert ar.calculate_volume(ar.map) == ar.volume
    assert ar.calculate_volume("abc") == None
    assert ar.calculate_volume(1) == None
    assert ar.calculate_volume(-1) == None
    assert ar.calculate_volume([1, 1]) == None
    assert ar.calculate_volume(["abc", "abc"]) == None
    assert ar.calculate_volume([True, True]) == None
    assert ar.calculate_volume(True) == None
    assert ar.calculate_volume(False) == None


def test_calculate_final_height():
    l = Limits.set_by_option("COM-C")
    ar = AccessibleRamp(height=3, width=1.2, option="COM-C", slope=8.33)

    assert ar.calculate_final_height(ar.map) == ar.final_heigth
    assert ar.calculate_final_height("abc") == None
    assert ar.calculate_final_height(1) == None
    assert ar.calculate_final_height(-1) == None
    assert ar.calculate_final_height([1, 1]) == None
    assert ar.calculate_final_height(["abc", "abc"]) == None
    assert ar.calculate_final_height([True, True]) == None
    assert ar.calculate_final_height(True) == None
    assert ar.calculate_final_height(False) == None