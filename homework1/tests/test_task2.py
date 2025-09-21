import src.task2 as t2
import pytest

@pytest.mark.parametrize(
        "op1, op2, exp",
        [
            (1,2,3),
            (1.0,2,3.0), 
            (1,2.0,3.0),
            (10**100,10**100, 2*10**100),
            (351, 69, 420),
            (1.1,2.2, 3.3000000000000003),
        ]
)
def test_addNum(op1, op2,exp):
    assert t2.addNum(op1,op2) == exp

@pytest.mark.parametrize(
        "op1, op2, exp",
        [
            (3,2,1),
            (3.0,2,1.0),
            (3,2.0,1.0),
            (0, 10**100, -10**100),
            (420, 69, 351),
        ]
)
def test_subNum(op1, op2,exp):
    assert t2.subNum(op1,op2) == exp


@pytest.mark.parametrize(
        "op1, op2, exp",
        [
            (3,2,6),
            (3.0,2,6.0),
            (3,2.0,6.0),
            (0, 10**100, 0),
        ]
)
def test_multNum(op1, op2,exp):
    assert t2.multNum(op1,op2) == exp


@pytest.mark.parametrize(
        "op1, op2, exp",
        [
            (6,2,3.0),
            (12,5,2.4),
            (10**100, 2*10**100, 0.5),
        ]
)
def test_div(op1, op2,exp):
    assert t2.div(op1,op2) == exp

@pytest.mark.parametrize(
        "op1, op2, exp",
        [
            (7,2,3),
            (-7,2,-4),
            (7,-2,-4),
            (7.0,2,3.0),
            (7,2.0,3.0),
            (7.5,2.3,3.0),
        ]
)
def test_floordiv(op1, op2,exp):
    assert t2.floorDiv(op1,op2) == exp


@pytest.mark.parametrize(
        "op1, op2, exp",
        [
            (7,2,1),
            (7,-2,-1),
            (-7,2,1),
        ]
)
def test_mod(op1, op2,exp):
    assert t2.modNum(op1,op2) == exp


@pytest.mark.parametrize(
        "op1, op2, exp",
        [
            ("hello","world","helloworld"),
            ("123","456","123456"),
            ("hello","","hello"),
            ("hello","    ","hello    "),
        ]
)
def test_cat(op1, op2,exp):
    assert t2.catStr(op1,op2) == exp


@pytest.mark.parametrize(
        "op1, op2, exp",
        [
            ("hello",2,"hellohello"),
            ("1-2-3-4-",4,"1-2-3-4-1-2-3-4-1-2-3-4-1-2-3-4-"),
            ("a",4,"aaaa"),
        ]
)
def test_rep(op1, op2,exp):
    assert t2.repStr(op1,op2) == exp


@pytest.mark.parametrize(
        "op1, op2, op3, op4, exp",
        [
            ("hello world", 3, None, None, 'l'),
            ("hello world", 0, None, None, 'h'),
            ("hello world", None, 4, None, 'hell'),
            ("hello world", None, None, 2, 'hlowrd'),
            ("hello world", None, None, -1, 'dlrow olleh'),
            ("hello world", 1, 5, 1, 'ello'),
        ]
)
def test_slice(op1, op2, op3, op4, exp):
    assert t2.sliceStr(op1,op2,op3,op4) == exp