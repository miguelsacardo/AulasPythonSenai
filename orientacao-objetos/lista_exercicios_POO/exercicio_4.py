'''
4. Classe Aluno. Crie uma classe Aluno com atributos nome e notas (lista de notas). 
Adicione o método media() para calcular e retornar a média das notas do aluno.
'''

#criação da classe
class Aluno:
    def __init__(self, nome):

        #atributos
        self.nome = nome
        self.notas = []

    #método média -> calcula e retorna a média das notas do aluno
    def media(self, obj_notas):
        self.notas.append(obj_notas)
        media = sum(self.notas)/len(self.notas)
        return media
    

#input usuário
nomeAluno =  str(input("Digite o nome do aluno: "))
quantidadeNotasAluno = int(input("Quantas notas vão ser escritas: "))

index = 0
while index < quantidadeNotasAluno:
    notasAluno = float(input("Insira as notas do aluno: "))
    index += 1

#instanciando a classe
media_aluno = Aluno(nomeAluno)

#imprimindo ao usuário
print(f"A média das notas do aluno {media_aluno.nome} é {media_aluno.media(notasAluno)}")

#instanciando a classe