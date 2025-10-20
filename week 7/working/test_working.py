import pytest
from working import convert

def test_empty():
    with pytest.raises(ValueError):
        convert("")

def test_invalid():
    with pytest.raises(ValueError):
        convert("12:60 AM to 13:50 PM")
    
    with pytest.raises(ValueError):
        convert("25 to 245")

def test_valid():
    assert convert("10:30 PM to 8 AM") == "22:30 to 08:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"