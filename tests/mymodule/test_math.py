from src.mymodule.math import exponential, factorial


def test_exponential():
    assert exponential(2, 3) == 8
    assert exponential(2, 0) == 1


factorial


def test_factorial():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120
