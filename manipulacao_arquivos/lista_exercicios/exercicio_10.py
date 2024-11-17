'''
10) Utilizando a biblioteca Pandas, leia a planilha "notas.xlsx" e imprima as informações na tela.
'''

#importando a biblioteca
import pandas as pd

#lendo o arquivo excel
df = pd.read_excel('manipulacao_arquivos/lista_exercicios/notas.xlsx', engine="openpyxl")

#exibindo o conteúdo
print(df)