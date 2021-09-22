import pytest

@pytest.mark.math
def test_one_plus_one():
    assert 1 + 1 == 2

@pytest.mark.math
def test_another_one():
    assert 1 + 3 == 4

@pytest.mark.math
def test_failing():
    a = 1
    b = 2
    c = 3
    assert a + b == c

@pytest.mark.math
def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError) as e:
        num = 1 / 0
    
    assert 'division by zero' in str(e.value)

# Multiplication test cases

# two positive integers
# identity: multiply a number by 1
# zero: multiply any number by 0
# positive by a number
# negative by a number
# multiply floats

products = [
    (2, 3, 6),
    (1, 99, 99),
    (3, -4, -12),
    (-5, -5, 25),
    (2.5, 6.7, 16.75)
]

@pytest.mark.parametrize('a, b, product', products)
def test_multiplication(a, b, product):
    assert a * b == product