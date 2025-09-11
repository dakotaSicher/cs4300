from src.task5 import threeBooks, studentInfo

def test_threeBooks():
    assert threeBooks() == [("Lady of the Empire", "Raymond E. Feist"),
    ("Basic Econimics", "Thomas Sowell"),
    ("Echoes of Honor", "David Weber"),]

def test_studentInfo():
    assert studentInfo(1)["firstName"] == "SpongeBob"
    assert studentInfo(2)["lastName"] == "Star"
    assert studentInfo(3)["Major"] == "Marine Biology"
    assert studentInfo(4) == {"firstName": "Squidward", "lastName": "Tentacles", "Major": "Clarinet"}
    