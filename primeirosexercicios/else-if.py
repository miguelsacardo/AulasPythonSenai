#aula if, else, elif
#ELSE -> qualquer outra condição que não for como a que foi especificada, vai ir pro else
#se uma condição é verdadeira, o if dessa condição é executado e ignora todo o resto do programa
#elif -> mais de uma opção

#pedir idade e verificar se é maior ou menor de idade
idade = int(input("Digite sua idade: "))

if idade < 18:
    print(f"Você é menor de idade! Idade informada: {idade}")
else:
    print(f"Você é maior de idade! Idade informada: {idade}")