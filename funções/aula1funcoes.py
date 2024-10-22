#código limpo, sem repetições
#bloco de código autônomo e reutilizável que é designado para realizar uma tarefa específica
#o corpo da função é um conjunto de instruções que são executadas quando a função é chamada
''' def nome_funcao(parametros)
        codigo
'''

#exemplo de função
def mensagem_boas_vindas():
    print("Bem vindo ao curso de programação")

mensagem_boas_vindas()

#return -> retornar alguma variável, quando eu quero usar a informação da função
def soma(a, b):
    resultado = a + b
    print(f"O resultado da soma é {resultado}")
    return resultado

#chamando a função
valor = soma(5,3)
print(f"Valor retornado: {valor}")

