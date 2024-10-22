'''5) Escreva uma função chamada contagem_regressiva() que recebe um número inteiro e faz uma contagem regressiva até 0, imprimindo cada número na tela.'''

def contagem_regressiva(numero):

    if numero < 0:
        return "Informe um número maior que zero."
    else:
        while numero >= 0:
            print("Contagem:", numero)
            numero -= 1


inputUsuario = int(input("Informe um número para ser feito uma contagem regressiva até 0."))
contagem_regressiva(inputUsuario)