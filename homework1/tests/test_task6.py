from src.task6 import countWords
import pytest

@pytest.mark.parametrize(
    "filepath,expected",
    [
        ("task6_read_me.txt",104),
        ("README.md",58),
    ]
)
def test_countWords(filepath, expected):
    assert countWords(filepath) == expected