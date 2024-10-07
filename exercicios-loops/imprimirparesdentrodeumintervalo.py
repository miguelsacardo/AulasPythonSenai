'''Imprimir os números pares dentro de um intervalo especificado
pelo usuário usando um loop for.'''

#entrada dos intervalos que o usuário deseja
inputInicioIntervalo = int(input("Digite o início do intervalo: "))
inputFinalIntervalo = int(input("Digite o final do intervalo: "))

'''o for faz ser exibido apenas os números pares do intervalo
que o usuário escreveu'''
for i in range(inputInicioIntervalo, inputFinalIntervalo + 1):
    if i%2 == 0:
        #exibe para o usuário
        print(i)