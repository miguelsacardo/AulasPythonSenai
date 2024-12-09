'''1) Crie uma função chamada conta_letras() que receba uma palavra como argumento e retorne um dicionário com a contagem de cada letra da palavra, exiba o dicionário.'''

def conta_letras(palavra):
    dict = {}
    lista_letras = []

    #verifica cada letra da palavra inserida
    for letras in palavra:
        
        #joga essas letras em uma lista
        lista_letras.append(letras.upper())

        # Ele vai contar as letras que aparecem mais de uma vez na lista, por isso o parâmetro passado é "letras" na função count.
        #isso acontece pois letras será interada pelo for, então o count pode checar cada letra
        quantidade = lista_letras.count(letras.upper())

        #joga em um dicionário para a letra ser a chave e o valor de repetição ser o valor
        dict[letras] = quantidade

    #mostra o dicionário
    print(dict)

#pede uma palavra ao usuário
palavra = str(input("Insira uma palavra para ser contada a quantidade de letras repetidas: "))

#chama a função
conta_letras(palavra)