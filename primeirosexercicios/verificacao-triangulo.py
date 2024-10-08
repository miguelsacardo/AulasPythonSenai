#verificar se um triângulo pode existir e classificá-lo
comprimento_1 = float(input("Informe o primeiro comprimento: "))
comprimento_2 = float(input("Informe o segundo comprimento: "))
comprimento_3 = float(input("Informe o terceiro comprimento: "))

verificar_primeira_soma = (comprimento_1 + comprimento_2) > comprimento_3
verificar_segunda_soma = (comprimento_1 + comprimento_3) > comprimento_2
verificar_terceira_soma = (comprimento_3 + comprimento_2) > comprimento_1

if verificar_primeira_soma == True and verificar_segunda_soma == True and verificar_terceira_soma == True:
    print(f"O triângulo pode existir.")

    if comprimento_1 == comprimento_2 and comprimento_1 == comprimento_3 and comprimento_2 == comprimento_3:
        print("O triângulo possui todos os lados iguais. Triângulo Equilátero.")
    elif comprimento_1 == comprimento_2 or comprimento_1 == comprimento_3 or comprimento_2 == comprimento_3:
        print(f"O triângulo possui ao menos dois lados iguais. Triângulo isóceles.")
    else:
        print(f"O triângulo não possui nenhum lado igual. Triangulo escaleno.")
else:
    print(f"O triângulo não pode existir.")
