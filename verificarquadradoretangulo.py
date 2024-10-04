#verificar se as medidas informadas são um quadrado ou um retângulo
medida_um = float(input("Digite a primeira medida: "))
medida_dois = float(input("Digite a segunda medida: "))
medida_tres = float(input("Digite a terceira medida: "))
medida_quatro = float(input("Digite a quarta medida: "))

#armazena todas as medidas em uma lista
medidas_geral = [medida_um,medida_dois,medida_tres,medida_quatro]

#verificar se há números iguais
if len(set(medidas_geral)) == 1:
    print(f"As medidas informadas são iguais, então a figura geométrica é um quadrado.\n")
    print(f"Medidas informadas: {medidas_geral}")
elif medidas_geral[0] == medidas_geral[2] and medidas_geral[1] == medidas_geral[3]:
    print(f"As medidas informadas podem formar um retângulo.")
    print(f"Medidas informadas: {medidas_geral}")
else:
    print("As medidas não podem formar um quadrado nem um retângulo.")