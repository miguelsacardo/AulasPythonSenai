'''2) Dado um arquivo .xls contendo dados referentes aos pedidos de compras de um e-commerce 
(arquivo gerado no desafio 1), sua tarefa é ler esse arquivo e converter
 seu conteúdo em um novo arquivo no formato .csv. Utilize a biblioteca pandas.'''

#importar bibliotecas
import pandas as pd

#ler o arquivo
df = pd.read_excel('manipulacao_arquivos/lista_exercicios/pedidos.xlsx', engine="openpyxl")
#exibir dados do arquivo
print(df)

#converter esse arquivo para o formato .csv
df.to_csv('manipulacao_arquivos/lista_exercicios/pedidos.csv', index=False)