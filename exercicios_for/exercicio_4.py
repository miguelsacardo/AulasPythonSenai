#tabuada de um número até 10

#input dos usuários
input_tabuada = float(input("DIgite um número: "))

#fazer a tabuada
for tabuada in range(1,11):
    multiplicacao = input_tabuada * tabuada
    print(f"{input_tabuada} * {tabuada} = {multiplicacao}")