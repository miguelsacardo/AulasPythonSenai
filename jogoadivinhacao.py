#jogo de adivinhação onde o porgrama escolhe um numero entre 1 a 10 e o jogador deve acertar com dicas

#importação de bibliotecas
import random

#sistema escolhe um número entre 1 a 10
escolha_sistema = random.randint(1,10)

#primeiro palpite do jogador
primeiro_palpite = int(input("Escreva seu primeiro palpite: "))


#dicas do sistema ou acerto
if escolha_sistema < primeiro_palpite:
    print("O número do sistema é MENOR que seu palpite.")

    # segundo palpite do jogador
    segundo_palpite = int(input("Escreva seu segundo palpite: "))

    # verificação do sistema final
    if segundo_palpite == escolha_sistema:
        print("Parabéns! Você conseguiu!")
    else:
        print(f"Você não conseguiu. Palpite 1: {primeiro_palpite}, segundo palpite: {segundo_palpite}. O número do sistema é: {escolha_sistema}")

elif escolha_sistema > primeiro_palpite:
    print("O número do sistema é MAIOR que seu palpite.")

    # segundo palpite do jogador
    segundo_palpite = int(input("Escreva seu segundo palpite: "))

    # verificação do sistema final
    if segundo_palpite == escolha_sistema:
        print("Parabéns! Você conseguiu!")
    else:
        print(f"Você não conseguiu. Palpite 1: {primeiro_palpite}, segundo palpite: {segundo_palpite}. O número do sistema é: {escolha_sistema}")


