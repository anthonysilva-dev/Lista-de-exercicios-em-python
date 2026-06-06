import pytest

from conversores import celsius_para_fahrenheit, fahrenheit_para_celsius

def test_celsius_para_fahrenheit1():
    assert celsius_para_fahrenheit(0) == 32

def test_celsius_para_fahrenheit2():
    assert celsius_para_fahrenheit(100) == 212

def test_fahrenheit_para_celsius():
    assert fahrenheit_para_celsius(32) == pytest.approx(0)

def test_fahrenheit_para_celsius2():
    assert fahrenheit_para_celsius(212) == pytest.approx(100)