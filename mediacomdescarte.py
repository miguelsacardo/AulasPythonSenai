#calcular média com descarte de notas de três provas (descartar a menor nota)
primeira_nota = float(input("Digite a primeira nota: "))
segunda_nota = float(input("Digite a segunda nota: "))
terceira_nota = float(input("Digite a terceira nota: "))

#verificar a menor nota
if primeira_nota < segunda_nota:
    maior_nota = segunda_nota
    menor_nota = primeira_nota
else:
    maior_nota = primeira_nota
    menor_nota = segunda_nota

#verificar a menor nota agora com a nota 3
if terceira_nota < maior_nota and terceira_nota < menor_nota:
    menor_nota = terceira_nota
elif terceira_nota > maior_nota and terceira_nota > menor_nota:
    maior_nota = terceira_nota

#calcular a média excluindo o valor
if primeira_nota == menor_nota:
    media = (segunda_nota + terceira_nota)/2
elif segunda_nota == menor_nota:
    media = (primeira_nota + terceira_nota)/2
else:
    media = (primeira_nota + segunda_nota)/2

#exibir ao usuário
print(f"O resultado da média é: {media}")
print(f"A nota excluída foi: {menor_nota}")
