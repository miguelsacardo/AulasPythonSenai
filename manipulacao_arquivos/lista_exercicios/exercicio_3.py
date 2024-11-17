'''3) Crie um arquivo CSV com o nome "alunos.csv" e insira as informações de dois alunos: 
João, 20 anos, e Maria, 22 anos.'''

#importando a biblioteca de csv
import csv

#dados do csv
dados = [
    ['Nome', 'Idade'],
    ['João', '20'],
    ['Maria', '22']
]

with open('manipulacao_arquivos/lista_exercicios/alunos.csv', 'w', newline='', encoding='utf-8') as arquivo:
    escritor_csv = csv.writer(arquivo)
    for linha in dados:
        escritor_csv.writerow(linha)


