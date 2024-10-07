'''Exibir a soma dos dígitos de um número fornecido pelo usuário
 usando um loop for.'''

inputNumero = int(input("Digite um número: "))

numeroString = str(inputNumero)

incrementador = 0
for i in numeroString:
    numeroInt = int(numeroString)
