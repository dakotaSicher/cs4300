from src.task7 import Crypter
import pytest

@pytest.mark.parametrize(
    "text",
    [
        ("Hello World"),
        ("123-56-7890")
    ]
)

def test_CrypterText(text):
    c = Crypter("password")
    encryptedText = c.encryptText(text)
    decryptedText = c.decryptText(encryptedText)
    assert text == decryptedText


@pytest.mark.parametrize(
    "filename",
    [
        ("task6_read_me.txt")
    ]
)

def test_CrypterFile(filename):
    c = Crypter("password")
    encFile = c.encryptFile(filename)
    decFile = c.decryptFile(encFile)

    with open(filename,"r") as org:
        orgText = org.read()
    with open(decFile, "r") as dec:
        decText = dec.read()
    assert orgText == decText