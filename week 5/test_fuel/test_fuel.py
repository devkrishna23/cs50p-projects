import pytest
from fuel import convert, gauge


def test_convert_0():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_convert_greater():
    with pytest.raises(ValueError):
        convert("4/3")

def test_convert_negative():
    with pytest.raises(ValueError):
        convert("-1/3")

def test_convert_invalid():
    with pytest.raises(ValueError):
        convert("a/2")

def test_convert_valid():
    assert convert("1/3") == 33

def test_gauge_full():
    assert gauge(99) == "F"

def test_gauge_empty():
    assert gauge(1) == "E"

def test_gauge_actual():
    assert gauge(75) == "75%"
 