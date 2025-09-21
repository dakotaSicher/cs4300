from src.task3 import sign,primesList,sumN
import pytest

@pytest.mark.parametrize(
        "op1, exp",
        [
            (1,"positive"),
            (-2, "negative"),
            (0, "zero"),
        ]
)
def test_sign(op1,exp):
    assert sign(op1) == exp

@pytest.mark.parametrize(
        "num, exp",
        [
            (10,[2,3,5,7,11,13,17,19,23,29])
        ]
)
def test_primesList(num, exp):
    assert primesList(num) == exp


@pytest.mark.parametrize(
        "num, exp",
        [
            (100, 100*101/2),
            (10, 10*11/2),
            (25, 25*26/2)
        ]
)
def test_sumN(num, exp):
    assert sumN(num) ==  exp