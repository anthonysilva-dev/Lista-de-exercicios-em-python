# Lista de Exercícios — Python

Exercícios desenvolvidos sem uso de classes, com funções separadas, tratamento de exceções e testes unitários com pytest.

## Q1 — Calculadora simples
Funções de soma, subtração, multiplicação e divisão. A função dividir lança ValueError para divisão por zero. Testes cobrem todas as operações incluindo o caso de divisão por zero com pytest.raises.

## Q2 — Validação de notas
Função validar_nota verifica se a nota está entre 0 e 10. A função calcular_media reutiliza validar_nota e lança exceção para notas inválidas. Testes cobrem notas válidas, inválidas e médias com casas decimais usando pytest.approx.

## Q3 — Conversão de temperatura
Funções de conversão entre Celsius e Fahrenheit implementadas em conversores.py e importadas em programa.py. pytest.approx é usado para lidar com imprecisão de ponto flutuante nas conversões.

## Q4 — Classificação de idade
Função validar_idade valida o intervalo de 0 a 120. A função classificar_idade reutiliza a validação antes de classificar em Criança, Adolescente, Adulto ou Idoso. O bloco if __name__ == '__main__' separa execução de importação.

## Q5 — Cálculo de frete
Função calcular_frete aplica as regras de negócio e lança exceções para peso ou distância inválidos. O programa principal está em main.py, separado da lógica de negócio em frete.py.
