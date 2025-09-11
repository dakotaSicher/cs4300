from src.task2 import dataType

def test_dataType():
    assert dataType(True) is bool
    assert dataType("hello") is str
    assert dataType(10) is int
    assert dataType(1.5) is float

    assert dataType([] is None) is bool
    assert dataType(10 + 1.0) is float
