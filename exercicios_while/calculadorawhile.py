isCalculatorOpen = True #define que o menu da calculadora está aberto

while isCalculatorOpen == True: #enquanto o menu da calculadora está aberto...
    operacao = input("Escolha '+' para soma, '-' para subtração e 'sair' para fechar a calculadora: ") #usuário escolhe uma operação ou sair da calculadora

    if operacao == "+":
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        resultado = num1 + num2
        print("soma: ",resultado) #exibe o resultado da soma para o usuário
    elif operacao == "-":
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        resultado = num1 - num2
        print("subtração: ",resultado) #exibe o resultado da subtração para o usuário
    elif operacao == "sair":
        isCalculatorOpen = False #se o usuário optar por sair, o menu da calculadora é definido como False, então o loop para
    else:
        print("Insira um valor válido ou saia da calculadora.") #se o usuário não digitar uma das 3 opções, o programa barra seu input