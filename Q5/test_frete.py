import pytest

from frete import calcular_frete

#Cálculo correto do frete
def test_calcular_frete_valido():
    assert calcular_frete(10, 20) == 45

#Peso inválido
def test_calcular_frete_peso_invalido():
    with pytest.raises(ValueError):
        calcular_frete(0, 20)

#Distância inválida
def test_calcular_frete_distancia_invalida():
    with pytest.raises(ValueError):
        calcular_frete(10, 0)

#Peso e distância inválidos
def test_calcular_frete_peso_e_distancia_invalidos():
    with pytest.raises(ValueError):
        calcular_frete(0, 0)