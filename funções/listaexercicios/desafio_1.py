'''1) Crie uma função chamada conta_letras() que receba uma palavra como argumento e retorne um dicionário com a contagem de cada letra da palavra, exiba o dicionário.'''

def conta_letras(palavra):
    dict = {}
    contagemLetras = 0
    for letras in palavra:
        dict['Letra'] = letras
        letraanterior = letras

        if letras == letraanterior:
           contagemLetras +=1
        print(dict)
        print(contagemLetras)
        print(letraanterior)


conta_letras("aab")