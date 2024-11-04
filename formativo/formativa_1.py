'''
Exercício: Sistema de Controle de Estoque Simplificado

Um armazém precisa de um programa para controlar o estoque de um produto específico. O usuário deve poder registrar novas quantidades de estoque, vender o produto e verificar o estoque atual.

O programa deve:

Perguntar ao usuário qual operação deseja realizar:
Adicionar (1),
Vender (2),
Verificar estoque (3),
Sair (4).
Usar um while para manter o programa em execução até que o usuário escolha a opção "Sair".
Utilizar if, elif, e else para controlar cada operação.
Para a operação de venda, usar um for para representar a venda de cada unidade do produto (ex: se o usuário escolheu vender 3 unidades, o for deve iterar 3 vezes, subtraindo uma unidade a cada passo).
Instruções para os alunos:

Inicialize o estoque como 0.
Verifique se o estoque é suficiente antes de realizar uma venda.
Exiba mensagens apropriadas para cada operação, como "Estoque insuficiente!" ou "Estoque atualizado!".
'''

#o usuário pode registrar novas quantidades de estoque, vender o produto e verificar o estoque atual
#while para manter o programa em execução ate escolher "sair"
#if, elif e else para controlar cada operação
#for para representar a venda de cada unidade do produto

#variável de estoque
estoque = 0

#1 - ) o while mantém  o programa em execução até escolher sair
while True:
    #escolha do usuário
    escolhaUsuario = int(input("Escolha uma opção: [1]ADICIONAR [2]VENDER [3]VERIFICAR ESTOQUE [4]SAIR\n"))

    if escolhaUsuario == 1:
        #adicionar produto
        adicaoProduto = int(input("Digite a quantida que você deseja adicionar no estoque: "))

        if adicaoProduto < 0:
            print("Informe um valor válido!")
        else:
            print("Estoque atualizado!")
            #adicionando produto
            estoque += adicaoProduto

    elif escolhaUsuario == 2:
       if estoque == 0:
           print("Você não tem produtos para vender!")
       else:
           quantidadeVenda = int(input("Quantos produtos você deseja vender?"))

           if quantidadeVenda > estoque:
               print("Você não possui essa quantia de produtos no estoque!")
           else:
               for i in range(quantidadeVenda):
                   print(i)


    elif escolhaUsuario == 3:
        #verificar estoque
        print(f"Você possui atualmente um estoque com {estoque} produto(s)")
    elif escolhaUsuario == 4:
        print("O programa foi parado.")
        break


