'''2) Crie uma função chamada maior_n() que recebe um número inteiro como argumento e retorna o maior número entre os n números digitados pelo usuário.'''

def maior_n(n): #recebe n números do usuário
    maior_numero = 0 #variável que irá armazenar o maior número
    contador = 0 #contador que será incrementado no While

    while contador < n: #enquanto o contador for menor que n números do usuário
        inputNumeros = float(input("Digite um número: "))

        #checa quais dos números informados é o maior
        if inputNumeros > maior_numero:
            maior_numero = inputNumeros
        contador += 1
    return maior_numero


n = int(input("Quantos números você deseja digitar?")) #entrada dos n números
print(maior_n(n)) #chamar a função



