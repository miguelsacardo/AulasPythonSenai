#crie uma classe Pessoa com atributos nome e idade e um método apresentar() que imprime o nome e a idade
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresetar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} ano(s) de idade.")

nome_pessoa = str(input("Qual é seu nome?"))
idade_pessoa = int(input("Qual é sua idade?"))
minha_apresentacao = Pessoa(nome_pessoa, idade_pessoa)
minha_apresentacao.apresetar()