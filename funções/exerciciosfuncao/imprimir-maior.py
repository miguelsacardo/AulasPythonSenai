#função para imprimir o maior de dois números. Crie uma função chamada maior() que recebe dois números como argumentos e retorna o maior deles

def maior(numero1, numero2):
    if numero1 == numero2: # se os números forem iguais, essa mensagem é retornada
        maior_numero = "Os números são iguais."

    elif numero1 > numero2: #se o número 1 for maior que o número dois, ele atribui para uma variável o numero1 como maior número
        maior_numero = f"O numero {numero1} é o maior"
    else: #senão, o numero2 é o maior número
        maior_numero = f"O número {numero2} é o maior"

    #retorna a variável contendo o maior número
    return maior_numero

numero1 = float(input("Informe o primeiro número: "))
numero2 = float(input("Informe o segundo número: "))

print(maior(numero1,numero2))

