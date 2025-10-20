from bank import value

def test_empty():
    assert value("") == 100

def test_Hello():
    assert value("Hello") == 0

def test_Hi():
    assert value("Hi") == 20

def test_text():
    assert value("What are you doing?") == 100