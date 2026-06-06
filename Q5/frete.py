def calcular_frete(peso, distancia):
    if peso <= 0 and distancia <= 0:
        raise ValueError("peso e distância inválidos.")
    if peso <= 0:
        raise ValueError("peso inválido.")
    if distancia <= 0:
        raise ValueError("distância inválida.")
    return 10 + peso * 2.50 + distancia * 0.50