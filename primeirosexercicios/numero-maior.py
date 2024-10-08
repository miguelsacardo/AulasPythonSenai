#verificar qual o maior número
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

if numero1 > numero2:
    print(f"O número {numero1} é maior que o número {numero2}")
elif numero1 == numero2:
    print(f"O número {numero1} é igual ao número {numero2}")
else:
    print(f"O número {numero1} é menor que o número {numero2}")