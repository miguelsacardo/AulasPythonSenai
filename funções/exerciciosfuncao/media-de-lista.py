#função para imprimir a média de uma lista de números. Crie uma função chamada media() que recebe uma lista de números como argumento e retorna a sua média

def media(lista_numeros):

    #variáveis que serão utilizadas no programa
    media = 0
    total = 0
    contador = 0
    lista = []

    while contador < tamanho_lista: #enquanto o contador for menor que o tamanho da lista, a função append() deve adicionar os elementos
        lista.append(lista_numeros)
        contador += 1

    for itens in lista:

        #a media deve ser uma variável vazia para ir somando aos valores dos itens da lista
        media += itens

        #no final, o total é a média dividida pelo tamanho da lista
        total = media/tamanho_lista

    #retorna a média
    return total

#contador que será utilizado no while de tamanho da lista
index = 0

#pergunta ao usuário o tamanho da lista que ele deseja, ou seja, quantos elementos a lista terá
tamanho_lista = float(input("Informe o tamanho da sua lista: "))

#enquanto o contador for menor que o tamanho da lista, é exibido os inputs pro usuário
while index < tamanho_lista:
    numeros_media = float(input("Digite os números da lista: "))
    index += 1

#chama a função
print(media(numeros_media))
