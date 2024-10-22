'''4) Escreva uma função chamada conta_vogais() que recebe uma string e retorna a quantidade de vogais (a, e, i, o, u) presentes na string.'''

def conta_vogais(palavra):
    quantidadeVogais = 0 #estabelece um contador de vogais como zero no início

    for letras in palavra: #o For irá verificar cada letra da String
        if letras.upper() == "A" or letras.upper() == "E" or letras.upper() == "I" or letras.upper() == "O" or letras.upper() == "U": #se alguma dessas condições forem verdadeiras, soma a quantidade de vogais
            quantidadeVogais += 1

    return quantidadeVogais


palavraUsuario = input("Digite uma palavra para verificar quantas vogais ela tem: ")
print(f"A palavra {palavraUsuario} tem {conta_vogais(palavraUsuario)} vogal(is)")