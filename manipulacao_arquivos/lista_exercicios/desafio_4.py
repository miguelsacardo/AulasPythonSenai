'''
4) DESAFIO SUPER MEGA POWER
Dada uma mensagem criptografada com a cifra de César e um deslocamento conhecido (3), 
seu objetivo é escrever um programa em Python 
para descriptografar a mensagem e recuperar o texto original contido no arquivo “criptografado.txt”.
'''

criptografia = open('manipulacao_arquivos/lista_exercicios/criptografia.txt', "r+", encoding='utf-8')

#contador
i = 0

#faz um loop que conta até 11. ELe vai até 11 por causa que o arquivo possui 11 linhas
while i < 11:

    #lê as linhas do arquivo
    linha1 = criptografia.readline()

    #lendo as linhas do documento
    for linhas in linha1:

        #encontra o valor unicode das linhas e subtrai 3 desse valor
        criptLinha1_depois = chr(ord(linhas) - 3)
        print(criptLinha1_depois)

    i += 1
    
#fecha o documento  
criptografia.close()

