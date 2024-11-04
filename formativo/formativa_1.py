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

#variáveis

#1 - ) o while mantém  o programa em execução até escolher sair
while True:
    #escolha do usuário
    escolhaUsuario = int(input("Escolha uma opção: [1]ADICIONAR [2]VENDER [3]VEFICIAR ESTOQUE [4]SAIR\n"))

    if escolhaUsuario == 1:
        pass
        #adicionar produto
    elif escolhaUsuario == 2:
        pass
        #vender
    elif escolhaUsuario == 3:
        pass
        #verificar estoque
    elif escolhaUsuario == 4:
        print("O programa foi parado.")
        break


