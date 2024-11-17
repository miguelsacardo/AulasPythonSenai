'''7) Crie um arquivo XML chamado "elementos.xml" 
e insira informações de dois elementos químicos: Hidrogênio e Oxigênio.'''

#importar biblioteca de XML
import xml.etree.ElementTree as ET

#contruindo xml Hidrogênio
root = ET.Element('Elementos')
elementoHidrogenio = ET.SubElement(root, 'Hidrogênio')
numeroAtomicoH = ET.SubElement(elementoHidrogenio, 'NúmeroAtômico').text = "1"
pesoAtomicoH = ET.SubElement(elementoHidrogenio, "PesoAtômico").text = "1.008"

#construindo xml Oxigênio
elementoOxigenio = ET.SubElement(root, "Oxigênio")
numeroAtomicoO = ET.SubElement(elementoOxigenio, "NúmeroAtômico").text = "8"
pesoAtomicoO = ET.SubElement(elementoOxigenio, "PesoAtômico").text = "15.999"

tree = ET.ElementTree(root)
tree.write("manipulacao_arquivos/lista_exercicios/elementos.xml", encoding='utf-8')

   
    