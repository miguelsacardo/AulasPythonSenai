'''
3) Contagem Regressiva. Crie uma função chamada contagem_regressiva que receba um número inteiro n. 
A função deve imprimir uma contagem regressiva a partir de n até 1 usando recursividade. Após a contagem, imprima “Fim”.
Observação: pesquise e utilize uma função recursiva.
'''

def contagem_regressiva(n):

    #a função deve ter essa checagem para não ficar um loop infinito
    try:
        if 1 <= n:
            print(n) #printa o numero até ele ser menor ou igual a um

        #retorna o n sendo decrementado por 1
        return contagem_regressiva(n-1)
    except Exception:
        return "Contagem finalizada!" #evita que seja printado um erro quando a contagem acaba

#pede o número ao usuário
numero_usuario = float(input("Digite um número para ser feita uma contagem regressiva: "))

#chama a função e passa o numero do usuário de parâmetro
print(contagem_regressiva(numero_usuario))
        
    