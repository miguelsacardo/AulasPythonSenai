#na orientação a objetos, temos classe e temos o objeto
#classe - esqueleto ou estrutura do que queremos criar
#classes podem ter atributos (características) e métodos (funções dentro de uma classe)
#objeto - instancia da classe
#eu só uso o init quando há atributos na classe

# class Cachorro:
#     def __init__(self, nome, idade):
#         self.nome = nome
#         self.idade = idade
#
#     def latir(self):
#         return "Au Au"
#
#     def idade_humana(self):
#         return self.idade * 7
#
#
# #criando o objeto cachorro
# meu_cachorro = Cachorro("Scooby", 5)
#
# #acessando os atributos e métodos do objeto
# print(meu_cachorro.latir())
#
# print(f"O nome do meu cachorro é {meu_cachorro.nome} ele tem {meu_cachorro.idade} ano(s) e sua idade humana é {meu_cachorro.idade_humana()}")

class Caneta:
    def __init__(self, cor):
        self.cor = cor
        self.tinta = 100

    def escrever(self):
        if self.tinta > 0:
            print(f"Escrevendo com a caneta {self.cor}")
            self.tinta -= 10 #gastar tinta
        else:
            print("Caneta sem tinta!")

    def recarregar(self):
        print("Recarregando a caneta")
        self.tinta = 100

    def verificar_tinta(self):
        return f"Tinta restante: {self.tinta}%"


#usando a classe caneta
minha_caneta = Caneta("azul") #saída = escrevendo com a caneta azul
minha_caneta.escrever()
print(minha_caneta.verificar_tinta()) #saída: tinta restante: 90%
minha_caneta.recarregar()

#escrever com a caneta 5 vezes
minha_caneta = Caneta("Vermelha")
quantidade_escrita = 0
while quantidade_escrita < 5:
    minha_caneta.escrever()
    quantidade_escrita += 1

print(minha_caneta.verificar_tinta())


#abstração: a classe cachorro serve como um modelo para criar objetos do tipo cachorro
class Cachorro:

    #encapsulamento: atributos são privados, só podem ser acessados ou modificados por métodos dentro da classe
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

        # método público para interagir com os atributos
    def get_nome(self):
        return self.nome

    def latir(self):
            print("Au Au!")

    #herança: Cachorro policial éuma extensão da classe Cachorro
class CachorroPolicial(Cachorro):
    def procurar_drogas(self):
        print("Procurando drogas...")


#polimorfismo: podemos tratar objetos de diferentes classes de maneira similar
def fazer_latir(nome_cachorro):
    nome_cachorro.latir()

rex = CachorroPolicial("Rex", 5)
rex.latir()
rex.procurar_drogas()

#polimorfismo exemplo: eu acesso o método latir() em uma função qualquer
fazer_latir(rex)