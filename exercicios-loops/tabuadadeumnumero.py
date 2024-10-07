'''Imprimir a tabuada de multiplicação de um número
fornecido pelo usuário usando um loop for.'''

#input do número que o usuário deseja ver a tabuada
inputNumeroUsuario = float(input("Digite um número para ver a tabuada: "))

#loop para exibir a tabuada
for tabuada in range(0,11):

    #exibindo para o usuário o resultado
    print(f"{inputNumeroUsuario} * {tabuada} = {inputNumeroUsuario * tabuada}")