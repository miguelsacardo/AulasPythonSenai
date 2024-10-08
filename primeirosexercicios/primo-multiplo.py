#verificar par ou impar e se é multiplo de 3 ou 5
numero = float(input("Digite um número: "))

if numero%2 == 0:
    print(f"O número {numero} é par")
else:
    print(f"O número {numero} é ímpar.")
if numero%3 == 0:
    print(f"O número {numero} é multiplo de 3.")
elif numero%5 == 0:
    print(f"O número {numero} é multiplo de 5.")
else:
    print(f"O número {numero} não é multiplo de 3 nem de 5.")