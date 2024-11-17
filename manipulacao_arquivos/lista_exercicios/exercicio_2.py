#2) Leia o arquivo "aula.txt" e imprima seu conteúdo na tela.

lerArquivo = open("manipulacao_arquivos/lista_exercicios/aula.txt","r", encoding="utf-8")

#lendo arquivo
print(lerArquivo.read())

#fecha o arquivo    
lerArquivo.close()