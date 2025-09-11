from src.task1 import helloWorld

def test_helloWorld(capsys):
    helloWorld()
    captured = capsys.readouterr()
    assert captured.out == "Hello, World\n"