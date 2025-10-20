from numb3rs import validate


def test_empty():
    assert validate("") == False

def test_valid():
    assert validate("255.255.255.255") == True

def test_less():
    assert validate("25.25.25") == False

def test_more():
    assert validate("25.25.25.25.25") == False

def test_first():
    assert validate("256.255.255.255") == False

def test_second():
    assert validate("255.256.255.255") == False

def test_third():
    assert validate("255.255.256.255") == False

def test_forth():
    assert validate("255.255.255.256") == False