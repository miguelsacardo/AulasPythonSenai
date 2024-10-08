#peça ao usuário 5 números e exiba o maior deles usando loop while

contagem = 0
maior = 0
while contagem < 5:
    input_numero = float(input("Digite um número: "))

    if input_numero > maior: #essa checagem tem que acontecer pois ele verifica se um número é maior que a variável "maior" e depois armazena se ele for
        maior = input_numero #isso é possível pois o while vai fazer os números serem contados então todos vão passar pelo if
    contagem += 1
print(maior)
