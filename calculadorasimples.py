#calculadora simples
primeiro_numero = float(input("Insira o primeiro número: "))
segundo_numero = float(input("Insira o segundo número: "))
operacao = input("Escolha uma operação: (+) Soma, (-) Subtração, (*) Multiplicação, (/) Divisão: ")

#escolher operacao e calcular

if operacao == "+":
    resultado = primeiro_numero + segundo_numero
elif operacao == "-":
    resultado = primeiro_numero - segundo_numero
elif operacao == "*":
    resultado = primeiro_numero * segundo_numero
elif operacao == "/":
    resultado = primeiro_numero / segundo_numero
else:
    print("Informe uma operação válida.")

print(f"O resultado da operação {primeiro_numero} {operacao} {segundo_numero} é igual a {resultado}")