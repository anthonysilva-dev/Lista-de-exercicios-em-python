import pytest

from cadastro import validar_idade, classificar_idade

#Idade válida
def test_validar_idade_valida():
    assert validar_idade(20)

#Idades inválidas
def test_validar_idade_invalida():
    with pytest.raises(ValueError):
        validar_idade(-5)
    with pytest.raises(ValueError):
        validar_idade(240)

#Classificações
def test_classificar_crianca():
    assert classificar_idade(11) == "Criança"

def test_classificar_adolescente():
    assert classificar_idade(17) == "Adolescente"

def test_classificar_adulto():
    assert classificar_idade(59) == "Adulto"

def test_classificar_idoso():
    assert classificar_idade(120) == "Idoso"