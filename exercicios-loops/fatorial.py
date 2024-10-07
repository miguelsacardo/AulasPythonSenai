#Calcular o fatorial de um número usando um loop while.

#input do número que o usuário quer saber o fatorial
inputNumeroFatorialUsuario = float(input("Digite o número que você deseja saber o fatorial: "))

n = 1 #número index que será multiplicado ao fatorial
fatorial = 1 #fatorial que será incrementado por fatorial *= n

if inputNumeroFatorialUsuario < 0:
    print("Digite um número positivo.")
else:
    while n <= inputNumeroFatorialUsuario:
        fatorial = fatorial * n
        n = n + 1

#exibir para o usuário
print(f"O fatorial de {inputNumeroFatorialUsuario} é {fatorial}")




