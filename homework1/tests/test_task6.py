from src.task6 import countWords

def test_countWords():
    assert countWords() == 104
    assert countWords("../README.md") == 8