def validar_idade(idade):
    if 0 <= idade <= 120:
        return True
    else:
        raise ValueError("idade inválida.")
        
def classificar_idade(idade):
    if validar_idade(idade) == True:
        if 0 <= idade < 12:
            classificacao = "Criança"
        elif 12 <= idade < 18:
            classificacao = "Adolescente"
        elif 18 <= idade < 60:
            classificacao = "Adulto"
        else:
            classificacao = "Idoso"
        return classificacao   

if __name__ == '__main__':
    try:
        idade = int(input("Digite sua idade: "))
        classificacao = classificar_idade(idade)
        print(f"Classificação: {classificacao}")
    except ValueError as e:
        if "invalid literal" in str(e):
            print("Erro: digite apenas números inteiros.")
        else:
            print(f"Erro: {e}")