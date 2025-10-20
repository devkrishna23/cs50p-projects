from um import count

def test_empty():
    assert count("") == 0

def test_not_um():
    assert count("yummy") == 0

def test_um():
    assert count("hello, um, world") == 1

def test_case():
    assert count("UM, Um, uM, um") == 4