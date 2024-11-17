'''8) Leia o arquivo "elementos.xml" e imprima as informações dos elementos na tela.'''

#importando a biblioteca
import xml.etree.ElementTree as ET

#carregar o arquivo e acessar sua estrutura
tree = ET.parse('manipulacao_arquivos/lista_exercicios/elementos.xml') #carrega o arquivo
root = tree.getroot() #acessa o elemento raiz 

#navegando pela estrutura
for child in root:
    print("\n",child.tag)
    for subelemento in child:
        print(subelemento.tag, subelemento.text)

    
        