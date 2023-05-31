import main

def test_add_positive_numbers():
    assert main.add_numbers(2, 3) == 5


def test_add_negative_numbers():
    assert main.add_numbers(-2, -3) == -5


def test_add_zero():
    assert main.add_numbers(-2, 0) == -2
