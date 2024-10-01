import pytest
from calc import add, subtract, multiply, divide, remainder

def test_add():
    assert add(10, 5) == 15
    assert add(-1, 1) == 0

def test_subtract():
    assert subtract(10, 5) == 5
    assert subtract(-1, -1) == 0

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(0, 10) == 0

def test_divide():
    assert divide(10, 2) == 5
    assert divide(10, 0) == "Erro: Divisão por zero!"

def test_remainder():
    assert remainder(10, 3) == 1
    assert remainder(10, 2) == 0
