from src.task3 import sign,primesList,sumN
import pytest

def test_sign():
    assert sign(1) == "positive"
    assert sign(10-12) == "negative"
    assert sign(0) == "zero"

    with pytest.raises(TypeError) as e: 
        sign("hello")
    assert e.type is TypeError

def test_primesList():
    assert primesList() == [2,3,5,7,11,13,17,19,23,29]

def test_sumN():
    assert sumN() ==  100*101/2