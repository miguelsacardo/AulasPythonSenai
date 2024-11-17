'''
3) Dado um arquivo .csv que contém dados referentes aos pedidos de compras de um e-commerce 
(arquivo gerado no desafio 2), sua tarefa é ler esse arquivo e converter seu conteúdo em 
um novo arquivo no formato .json. Utilize a biblioteca pandas para realizar essa operação.
'''

#importando bibliotecas
import pandas as pd
import json

#ler o arquivo .csv
df = pd.read_csv('manipulacao_arquivos/lista_exercicios/pedidos.csv')
#exibir dados
print(df)

#serializar para json
df.to_json('manipulacao_arquivos/lista_exercicios/pedidos.json', indent=4, force_ascii=False)
