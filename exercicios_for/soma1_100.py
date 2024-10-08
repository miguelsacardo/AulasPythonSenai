#faça um programa que calcule a soma dos números de 1 a 100

soma = 0 #crio uma variável "soma" que recebe zero.
for numeros_primeiro in range(1,101): #o FOR faz uma contagem do número 1 até 100.
    soma = numeros_primeiro + soma #soma é incrementada a cada número que passa
    print(soma)


#primeiro FOR = soma é 0 e o numeros_primeiro é 1, então 1 + 0 = 1
#segundo FOR = soma é 1 e o numeros_primeiro é 2, então 2 + 1 = 3





