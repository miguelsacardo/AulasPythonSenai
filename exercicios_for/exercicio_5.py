#programa que exiba a média de uma lista de números
input_tamanho = int(input("Digite o tamanho da lista: "))
lista = [] #lista vazia

for i in range(input_tamanho): #o +1 no rand para saber que ele tem que ir até o número do usuário, e nao um a menos
    item = int(input("Digite 1 item da lista: "))
    lista.append(item) #adiciono "n" a lista

media  = sum(lista) / len(lista) #aqui eu somo os itens da lista (sum) e divido-os pelo tamanho da lista (len)
print(f"A média dos itens da lista é: {media}")