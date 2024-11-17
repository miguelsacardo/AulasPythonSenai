'''4) Leia o arquivo "alunos.csv" e imprima as informações dos alunos na tela.'''

#importando a biblioteca de csv
import csv

with open('manipulacao_arquivos/lista_exercicios/alunos.csv', encoding='utf-8') as arquivo:
    leitor_csv = csv.reader(arquivo)
    for linha in leitor_csv:
        print(linha)