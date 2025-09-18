from src.task4 import calculate_discount
import pytest

@pytest.mark.parametrize(
    "price,discount,expected",
    [
        (100,10,90),
        (49.99,25.8,37.09),
        (841.38,50,420.69),
    ]
)
def test_calculate_discount(price,discount,expected):
    assert calculate_discount(price, discount) == expected


def test_calc_disc_except():
    with pytest.raises(TypeError):
        calculate_discount("100", 25.5) 