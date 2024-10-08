#digite um numero de 5 a 10 e exiba a contagem regressiva

input_numero = float(input("Digite um número de 5 a 10: ")) #entrada de dados

if input_numero < 5 or input_numero > 10: #checa se o número informado é de 5 a 1-
    print("Informe um número de 5 a 10.")
else:
    while input_numero >= 0: #executa a contagem regressiva
        print(f"Contagem regressiva: {input_numero}")
        input_numero = input_numero - 1