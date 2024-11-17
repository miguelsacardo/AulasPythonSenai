'''Excel (.xlsx) usando Pandas
9) Utilizando a biblioteca Pandas, crie uma planilha do Excel chamada "notas.xlsx" e 
insira as notas de dois alunos nas disciplinas de Matemática e Português.'''

#importando pandar
import pandas as pd
import os

#dados do xlsx
data = {
    'Matérias':['Matemática','Português'],
    'Aluno1':['10.0','5.0'],
    'Aluno2':['7.5','2.0']
}

#arquivo será convertido em excel
df = pd.DataFrame.from_dict(data)

# print(caminho_atual)
df.to_excel('manipulacao_arquivos/lista_exercicios/notas.xlsx', index=False)