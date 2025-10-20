import pytest
from seasons import main 


def test_example(monkeypatch, capsys):

    monkeypatch.setattr("builtins.input", lambda _: "2000-01-01")

    main()
    captured = capsys.readouterr()
    assert "minutes" in captured.out.lower()
