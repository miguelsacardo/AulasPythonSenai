'''Ler uma sequência de números do usuário
e determinar o maior e o menor número usando um loop while.'''

#input da quantidade de números que o usuário deseja
inputQuantidadeNumeros = int(input("Digite a quantidade de números que você deseja: "))

#contador do while
index = 0

#define as variáveis maior e menor como "None", se for 0 ou "" vai dar erro
numeroMaior = None
numeroMenor = None

while index < inputQuantidadeNumeros:

    #solicita os números com base na quantidade de números que o usuário quer
    inputNumerosUsuario = float(input("Digite um número: "))

    #caso as variáveis maiores e menores forem None, inicializa elas com o valor do número do usuário
    if numeroMaior == None and numeroMenor == None:
        numeroMaior = inputNumerosUsuario
        numeroMenor = inputNumerosUsuario

    #verifica se o número digitado pelo usuário é o maior
    if inputNumerosUsuario > numeroMaior:
        numeroMaior = inputNumerosUsuario

    #verifica se o número digitado pelo usuário é o menor
    if inputNumerosUsuario < numeroMenor:
        numeroMenor = inputNumerosUsuario

    index += 1

#exibe ao usuário
print(f"O número maior é {numeroMaior} e o número menor é {numeroMenor}")



