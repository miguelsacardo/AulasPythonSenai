#pedra, papel e tesoura
import random #import de biblioteca

opcao_jogador = input("Escreva seu movimento - Pedra, Papel Tesoura: ")
opcao_computador = random.choice(["pedra","papel","tesoura"]) #arrays jogada do computador

if opcao_jogador == opcao_computador:
    print(f"Empate! Jogador: {opcao_jogador} \n Computador: {opcao_computador}")
elif opcao_jogador == "pedra" and opcao_computador == "tesoura":
    print(f"Vitória do jogador! Jogador: {opcao_jogador} \n Computador: {opcao_computador}")
elif opcao_jogador == "papel" and opcao_computador == "pedra":
    print(f"Vitória do jogador! Jogador: {opcao_jogador} \n Computador: {opcao_computador}")
elif opcao_jogador == "tesoura" and opcao_computador == "papel":
    print(f"Vitória do jogador! Jogador: {opcao_jogador} \n Computador: {opcao_computador}")
else:
    print(f"Vitória do computador! Computador: {opcao_computador} \n Jogador: {opcao_jogador}")
