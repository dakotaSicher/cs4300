from src.task7 import Crypter, encryptFile,decryptFile
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
    
    encFile = encryptFile(filename, "password")
    decFile = decryptFile(encFile, "password")

    with open(filename,"r") as org:
        orgText = org.read()
    with open(decFile, "r") as dec:
        decText = dec.read()
    assert orgText == decText