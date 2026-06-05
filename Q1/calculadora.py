def exibir_mensagem():
    print('Calculadora simples em Python')
def somar(a, b):
    return a + b
def subtrair(a, b):
    return a - b
def multiplicar(a, b):
    return a * b
def dividir(a,b):
    if b == 0:
        raise ValueError("Erro: o divisor não pode ser zero")
    else:
        return a / b
