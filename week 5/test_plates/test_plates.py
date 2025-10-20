from  plates import is_valid

def test_empty():
    assert is_valid("") == False

def test_length():
    assert is_valid("C") == False
    assert is_valid("vsfvdsaf") == False

def test_zero():
    assert is_valid("CS05") == False

def test_valid():
    assert is_valid("CS50") == True

def test_invalid():
    assert is_valid("CS50P") == False

def test_special():
    assert is_valid("$") == False

def test_start():
    assert is_valid("50CS") == False
    assert is_valid("CS50") == True