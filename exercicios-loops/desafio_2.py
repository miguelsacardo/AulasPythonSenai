'''
2) Simulação de Populações de Coelhos

Crie um programa que simule o crescimento de uma população de coelhos ao longo de várias gerações. 
Os coelhos se reproduzem a uma taxa fixa a cada geração, e uma porcentagem deles morre a cada geração.
O programa deve solicitar ao usuário a taxa de reprodução, a taxa de mortalidade e o número inicial de coelhos. 
Use um loop for ou while para simular várias gerações e exiba a população de coelhos após um número de gerações especificado pelo usuário.
'''

#taxa repro (porcentagem)
#taxa mortalidade (porcentagem)
#numero inicial
#tempo
POPULACAO_INICIAL = int(input("Digite o número da população inicial de coelhos: "))
TAXA_REPRODUCAO = float(input("Digite a taxa de reprodução dos coelhos: "))/100
TAXA_MORTALIDADE = float(input("Digite a taxa de mortalidade dos coelhos: "))/100
GERACOES = int(input("Digite quantas gerações você deseja visualizar: "))
equacao = POPULACAO_INICIAL

for i in range(1, GERACOES):
    equacao +=  (POPULACAO_INICIAL * TAXA_REPRODUCAO) - (POPULACAO_INICIAL * TAXA_MORTALIDADE)
    print(f"Geração {i + 1} | População {equacao}")
