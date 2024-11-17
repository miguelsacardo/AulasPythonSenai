'''6) Leia o arquivo "info.json" e imprima as informações dos animais na tela.'''

#importando a biblioteca de JSON
import json

#deserializar o JSON em um objeto python
with open("manipulacao_arquivos/lista_exercicios/info.json", "r") as json_file:
    dados = json.load(json_file)
    
#mostrando os dados
print(dados)
