'''
1) Jogo da Forca.
Crie um jogo da forca em que um jogador escolhe uma palavra e outro jogador tenta adivinhar a palavra,
fornecendo letras. O jogador tem um número limitado de tentativas e uma parte da forca é desenhada após cada tentativa incorreta. 
Use um loop while para controlar as tentativas e uma combinação de for e if para verificar as letras na palavra.
'''

#declaração de variáveis
palavra = str(input("Digite a palavra que será utilizada no jogo: "))
letras_usuario = []
chances = 5
ganhou = False


while True: 
    for letra in palavra:

        #verifica se a letra foi uma das que o usuário chutou
        if letra.lower() in letras_usuario:
            print(letra, end="") #imprime tudo em uma mesma linha

        #se o usuário não tiver chutado nenhuma, exibe apenas "_" ocultando a palavra
        else:
            print("_", end="")

    #exibe as chances restantes
    print(f"\nVocê tem {chances} chances")

    #pede para o usuário uma letra e coloca ela na lista das letras que o usuário informa
    tentativa = str(input("Escolha uma letra para adivinhar: "))
    letras_usuario.append(tentativa.lower())

    #se a letra que o usuário chutou não bate com nenhuma da palavra, suas chances são decrementadas
    if tentativa.lower() not in palavra.lower():
        chances -= 1

        if chances == 4:
            print("O")
        elif chances == 3:
            print("""
             O
            /|\  
                  """)
        elif chances == 2:
            print("""
             O
            /|\  
            /      """)
        elif chances == 1:
            print("""
             O
            /|\  
            / \     """)
        elif chances == 0:
            print("""
             O
            ---
            /|\  
            / \     """)
    ganhou = True

    #o jogador perde se na lista das letras chutadas não houver nenhuma letra que a palavra possui
    for letra in palavra:
        if letra.lower() not in letras_usuario:
            ganhou = False

    if chances == 0 or ganhou:
        break

if ganhou:
    print(f"Parabéns, você ganhou! A palavra era: {palavra}")
else:
    print(f"Você perdeu. A palavra era {palavra}")

