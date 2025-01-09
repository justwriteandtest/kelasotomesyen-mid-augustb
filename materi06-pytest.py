import pytest

products = [
    (2, 3, 6),
    (1, 99, 99),
    (0, 99, 0),
    (3, -4, -12),
    (5, 5, 25),
    (2.5, 6.7, 16.75)
]

@pytest.mark.parametrize("a, b, c", products)
def test_multiplication(a, b, c):
    assert a * b == c