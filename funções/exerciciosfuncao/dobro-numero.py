#função para imprimir o dobro de um número. Crie uma função chamada dobro() que recebe um número como argumento e retorna seu dobro

#função que recebe o input como parâmetro=
def dobro(numero):
    dobro = numero * 2 #faz o calculo do dobro do número
    return dobro #retorna o valor do dobro
#pede pro usuário o número que ele quer calcular o dobro

numero = float(input("Digite o número desejado: "))
print(f"O dobro do número {numero} é {dobro(numero)}")