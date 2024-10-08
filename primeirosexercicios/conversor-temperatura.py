#programa que permite o usuário escolher entre converter uma temperatura de celsius para fahrenheit ou vice versa
tipo = input("Digite o tipo desejado (c) para celcius e (f) para fahrenheit: ")

if tipo == "c" or tipo == "C":
    temperatura = float(input("Digite a temperatura em fahrenheit: "))
    celcius = (temperatura - 32) * 5/9
    print(f"A temperatura em celcius é {celcius}°C")
elif tipo == "f" or tipo == "F":
    temperatura = float(input("Digite a temperatura em celcius: "))
    fahrenheit = (temperatura * 9/5) + 32
    print(f"A temperatura em fahrenheit é {fahrenheit}°F")
else:
    print(f"Informe um tipo válido.")