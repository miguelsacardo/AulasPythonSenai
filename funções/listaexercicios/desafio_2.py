'''
2) Crie uma função chamada ordena_lista() que receba uma lista de números e 
retorne essa lista ordenada de forma crescente, sem usar funções internas de ordenação.'''


def ordena_lista(quantidade):
    lista = []

    #deverá executar de acordo com a quantidade de números que o usuário desejar
    for x in range(quantidade):

        #pede os números para o usuário
        numeros = float(input("Digite um número: "))

        #variável de checagem para ver se o numero foi inserido
        inseriu = False

        #ordena os números que o usuário informar
        for i in range(len(lista)):
            if numeros < lista[i]:
                lista.insert(i, numeros)

                #essa variável evita que o valor seja duplicado na lista
                inseriu = True
                break
        
        #ese trecho é necessário para garantir que os numeros sejam corretamente colocados na lista
        if not inseriu:
            lista.append(numeros)

        #mostra a lista ordenada
        print(lista)
   
#pede ao usuário a quantidade de números que ele deseja inserir 
input_quantidade = int(input("Quantos números você deseja inserir na lista? "))

#chama a função
ordena_lista(input_quantidade)