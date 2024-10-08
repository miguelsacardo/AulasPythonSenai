#for e while -> repete instruções várias vezes, até a condição ser falsa
#for -> serve para conjuntos (agrupamento de coisas)
#for -> para cada item dentro de um conjunto
#exemplo:  for item in conjunto
#conjuntos são finitos

#estrutura for
#for cada_elemento in um_conjunto -> se eu tenho um conjunto com mil, ele vai executar mil vezes
#para cada elemento nesse conjunto, eu faço uma condição...
#tipos de conjuntos no python -> listas (são um conjunto), uma frase string é um conjunto de caracteres (o espaço também conta como um caractere)
#tipos de conjuntos no python -> tuplas (semelhante a uma lista,mas não consegue adicionar e nem remover itens da tupla)
#tipos de conjuntos no python -> dicionário: coleção de pares chave-valor onde cada chave é única e associada a um valor, você pode interar pelas chaves, pelos valores ou pelos pares chave-valor
#tipos de conjuntos no python -> conjuntos (conjunto chamado conjunto): coleção de elementos únicos, sem ordem específica (são iteráveis)
#tipos de conjuntos no python -> range (predefinido, do número que começa até o número que ele vai) é sempre um número a menos que o final. Muito usado em loops FOR para criar intervalos numéricos
#podemos escrever o range como range(10): 0 ao 9. Outra forma range(1,101,2): do 1 ao 100 contando de 2 em 2

#outros objetos iteráveis -> ao abrir um arquivo em python, você pode iterar pelas linhas ou caracteres do arquivo
#exemplo FOR -> listas
frutas = ['maçãs', 'banana', 'laranja']
for fruta in frutas:
    print(fruta)

#exemplo FOR -> frases String
mensagem = "Hello World"
for caractere in mensagem:
    print(caractere)

#exemplo FOR -> tuplas
cores = ("vermelho", "verde", "azul", "amarelo")
for cor in cores:
    print("Cor:", cor)

#exemplo FOR -> dicionário
#variáveis que começam com {} -> pode ser um dicionário (o python sabe que é pelos pontos no meio)
pessoa = {
    "Nome": "Ana",
    "Idade": 18,
    "Profissão": "Engenheira"
}
for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")

#exemplo FOR -> conjuntos
#variáveis que começam com {} -> pode ser um conjunto, mas segue o modelo como {1,5,3,...}
animais = {"gato", "cachorro", "elefante", "girafa"}
for animal in animais:
    print("Animal:", animal)

print("\n")

#exemplo FOR -> range(5): 0 ao 4
for numero in range(5):
    print("Exemplo 1: ",numero)

print("\n")

#exemplo FOR -> range(1,11): 1 ao 10
for numero in range(1,11):
    print("Exemplo 2: ",numero)

print("\n")

#exemplo FOR -> range(0,11,2): 0 ao 10 contando de 2 em 2
for numero in range(0,11,2):
    print("Exemplo 3: ",numero)

print("\n")

#exemplo FOR -> range(0,11,3): 0 ao 10 contando de 3 em 3
for numero in range(0,11,3):
    print("Exemplo 4: ",numero)

print("\n")

#ler linhas de um arquivo txt
nome_arquivo = "C:/Users/51773121863/Desktop/aulas-marcia/lacosderepeticao/exemplolerarquivo.txt"
with open(nome_arquivo, "r", encoding="utf-8") as arquivo: #"open with" -> sintaxe da abertura de arquivos
    for linha in arquivo:
        print(linha.strip()) #strip() remove espaços em branco