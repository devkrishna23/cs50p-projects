from twttr import shorten

def test_empty():
    assert shorten("") == ""

def test_upper():
    assert shorten("App") == "pp"

def test_lower():
    assert shorten("app") == "pp"

def test_digits():
    assert shorten("1 is one") == "1 s n"

def test_special():
    assert shorten("$ is dollar sign") == "$ s dllr sgn"

def test_punc():
    assert shorten(", is a good thing") == ", s  gd thng"