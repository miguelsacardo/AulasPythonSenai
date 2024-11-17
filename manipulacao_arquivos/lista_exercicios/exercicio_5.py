'''
5) Crie um arquivo JSON chamado "info.json" e insira informações de dois animais: 
um gato chamado Felix e um cachorro chamado Rex.
'''

#importando a biblioteca para JSON
import json

#dados que irão ser inseridos no json
animais = {
    "animais":[
        {
            'cachorro':'Rex',
            'gato':'Felix'
        }
    ]
}

#serializar para json
with open("manipulacao_arquivos/lista_exercicios/info.json", "w") as json_file:
    json.dump(animais, json_file, indent=4) #o dump recebe dois argumentos obrigatórios -> o objeto a ser serializado e o arquivo que ele será gravado
    #o terceiro argumento é a indentação do JSON -> melhora a visualização do arquivo