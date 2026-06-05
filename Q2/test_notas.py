import pytest

from notas import validar_nota, calcular_media

#Nota válida
def test_validar_nota():
    assert validar_nota(8) == True

#Nota inválida
def test_validar_nota_invalida():
    assert validar_nota(12) == False

#Média válida
def test_calcular_media():
    assert calcular_media(9, 8, 7) == 8
    
def test_calcular_media2():
    with pytest.raises(ValueError):
        calcular_media(10, 12, 8)