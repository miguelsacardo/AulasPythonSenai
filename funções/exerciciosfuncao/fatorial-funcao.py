#crie uma função chamada calcular_fatorial que receba um número inteiro como parâmetro e retorne o fatorial desse número. Exiba o resultado ao final.

def calcular_fatorial(numero_fatorial):
    fatorial = 1
    index = 1
    while index <= numero_fatorial:
        fatorial = fatorial * index
        index = index + 1
    return fatorial

inputFatorial = int(input("Digite o número que você quer saber o fatorial: "))
print(f"O fatorial do número {inputFatorial} é {calcular_fatorial(inputFatorial)}")