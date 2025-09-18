from src.task2 import dataType,add,sub, mult, div, mod
import pytest

def test_dataType():
    assert dataType(True) is bool
    assert dataType("hello") is str
    assert dataType(10) is int
    assert dataType(1.5) is float

    assert dataType([] is None) is bool
    assert dataType(10 + 1.0) is float

def test_nums():
    assert add(1,1) == 2
    assert add(1.1,1) == 2.1
    assert add(2.1,4.8) == 6.9

    assert sub(2,1) == 1

    #Floats have precision that sometimes give weird results
    assert add(1.1, 2.2) != 3.3
    assert sub(3.3, 1.1) != 2.2
    

    assert mult(2,2) == 4
    assert mult(2.0, 2.0) == 4.0

    assert div(10,2) == 5
    assert div(10,2.5) == 4

    assert mod(12,5) == 2
    #again floats be funky
    assert mod(2.2,1) != 0.2

    #int can be cast to float
    assert float(1) == 1.0
    #but if you go float to int then you lose the decimal
    assert int(1.1) == 1



def test_strings():
    #strings can be added (concatenated)
    assert add("hello","world") == "helloworld"
    
    #doesn't covert to string
    with pytest.raises(TypeError):
        add("hello",15)

    #even if its a number
    with pytest.raises(TypeError):
        add("100",15) == 115

    #strings of numbers can be cast tho if they match
    assert add(int("100"),15) == 115
    assert add(float("1.1"),2) == 3.1
    #if they match what you try to cast them too
    with pytest.raises(ValueError):
        add(int("1.1"), 2)

    #but '+' is all that works
    with pytest.raises(TypeError):
        sub("hello","ello")
    with pytest.raises(TypeError):
        mult("hello","world")
    with pytest.raises(TypeError):
        div("hello","world")

def test_bool():
    #what does adding bools do?
    assert add(True, True) == 2

    #bools are basically just int 0 or 1
    assert add(True, False) == True
    assert add(True, False) == 1
    assert add(1,False) == True
    assert add(0,0) == False

