'''Exibir a soma dos dígitos de um número fornecido pelo usuário
 usando um loop for.'''

#pede um número em formato de str para poder ser interado
inputNumero = str(input("Digite um número: "))
lista_digito = []

for i in inputNumero:

    #joga os digitos em uma lista
    lista_digito.append(int(i))

#soma dos digitos
print(f"A soma dos digitos desse número é : {sum(lista_digito)}")
    
    
