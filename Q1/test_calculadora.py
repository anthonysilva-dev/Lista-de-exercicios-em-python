import pytest
from calculadora import somar, subtrair, multiplicar, dividir

def test_somar():
    assert somar(10, 4) == 14

def test_subtrair():
    assert subtrair(22, 8) == 14

def test_multiplicar():
    assert multiplicar(7, 2) == 14

def test_dividir():
    assert dividir(28, 2) == 14

def test_dividir_por_zero():
    with pytest.raises(ValueError):
        dividir(10, 0)