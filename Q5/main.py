from frete import calcular_frete

if __name__ == '__main__':
    try:
        peso = float(input("Digite o peso (kg) da carga: "))
        distancia = float(input("Digite a distância (km) do trajeto: "))
        calculo=calcular_frete(peso, distancia)

        print(f"Valor do frete: R${calculo:.2f}")

    except ValueError as e:
        if "could not convert string to float" in str(e):
            print("Erro: apenas números são permitidos.")
        else:
            print(f"Erro: {e}")