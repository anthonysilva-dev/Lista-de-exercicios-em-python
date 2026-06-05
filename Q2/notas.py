def validar_nota(nota):
    if 0 <= nota <= 10:
        return True
    else:
        return False

def calcular_media(nota1, nota2, nota3):
    if validar_nota(nota1) and validar_nota(nota2) and validar_nota(nota3):
        return (nota1 + nota2 + nota3) / 3
    else:
        raise ValueError("Erro: nota inválida.")
    