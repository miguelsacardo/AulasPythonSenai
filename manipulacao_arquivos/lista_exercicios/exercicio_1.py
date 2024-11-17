'''
TXT (.txt)

1) Enunciado: Crie um arquivo de texto chamado "aula.txt" e escreva nele as frases 
"Python é legal!" e "Aprendendo manipulação de arquivos".
'''

arquivoTxt = open("manipulacao_arquivos/lista_exercicios/aula.txt", "w", encoding="utf-8")
arquivoTxt.write("Python é legal!\n")
arquivoTxt.write("Aprendendo manipulação de arquivos")

arquivoTxt.close()