from src.task4 import calculate_discount
import pytest

def test_calculate_discount():
    assert calculate_discount(100, 10) == 90
    assert calculate_discount(49.99, 25.8) == 37.09
    assert calculate_discount(841.38, 50) == 420.69
    assert calculate_discount("100.0", 10.5) == 89.5

    with pytest.raises(Exception) as e:
        calculate_discount("Five hundred cigarettes", 25.5) 
    assert e.type is ValueError