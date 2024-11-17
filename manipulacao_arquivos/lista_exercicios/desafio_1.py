'''
1) Dado um conjunto de dados referente aos pedidos de compras de um e-commerce,
armazenado em uma lista de dicionários no Python, sua tarefa é gerar 
um arquivo .xls a partir desses dados. Utilize a biblioteca pandas para realizar essa operação.
'''
#importação de bibliotecas
import pandas as pd

#dados do arquivo
historico_pedidos = [

    {'ID': 1, 'Nome': 'João', 'Endereço': 'Rua das Flores, 123', 'Produto': 'Camiseta', 'Quantidade': 2, 'Preço': 50, 'Data': '01/01/2023'},

    {'ID': 2, 'Nome': 'Mariana', 'Endereço': 'Avenida Central, 456', 'Produto': 'Tênis', 'Quantidade': 1, 'Preço': 120, 'Data': '02/01/2023'},

    {'ID': 3, 'Nome': 'Carlos', 'Endereço': 'Praça da Estação, 789', 'Produto': 'Mochila', 'Quantidade': 1, 'Preço': 80, 'Data': '03/01/2023'},

    {'ID': 4, 'Nome': 'Fernanda', 'Endereço': 'Alameda dos Anjos, 101', 'Produto': 'Relógio', 'Quantidade': 1, 'Preço': 150, 'Data': '04/01/2023'}
]

#arquivo será convertido em excel
df = pd.DataFrame(historico_pedidos)

#gerando xlsx dos dados
df.to_excel('manipulacao_arquivos/lista_exercicios/pedidos.xlsx', index=False)