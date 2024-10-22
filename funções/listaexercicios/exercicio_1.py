'''1) Calculadora de IMC. Crie uma função que calcule o Índice de Massa Corporal (IMC) de uma pessoa. A fórmula do IMC é:'''

#criar função com os parâmetros peso e altura, o que é necessário para calcular o IMC
def IMC (peso, altura):
   calculoIMC = peso / altura  ** 2
   return calculoIMC

#pede os parâmetros pro usuário
inputPeso = float(input("Digite seu peso: "))
inputAltura = float(input("Digite sua altura: "))

print(f"O seu IMC é {IMC(inputPeso,inputAltura)}")