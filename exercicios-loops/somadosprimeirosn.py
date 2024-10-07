'''2) Calcular a soma dos primeiros N números naturais,
 onde N é fornecido pelo usuário, usando um loop while.'''

inputNumeroUsuario = int(input("Forneça um número para ser calculado a soma dos números até ele: "))

#contador
i = 0

#numero que será incrementado
n = 0

while i <= inputNumeroUsuario:
    n += i #incrementação de n
    i+=1

#exibindo ao usuário
print(n)