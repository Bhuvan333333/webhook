import pytest
from calculator import add,sub,mul

def test_add():
    addition = add(2,2)
    assert addition == 4

def test_sub():
    subtraction = sub(2,2)
    assert subtraction == 0


def test_mul():
    multiplication = mul(2,2)
    assert multiplication == 5

