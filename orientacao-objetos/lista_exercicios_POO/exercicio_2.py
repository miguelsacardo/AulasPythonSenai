'''
2. Classe Carro. Crie uma classe Carro com atributos modelo, ano e quilometragem. 
Adicione o método detalhes() que imprime todas as informações do carro.
'''

#criação da classe
class Carro:
    def __init__(self, modelo, ano, quilometragem):

        #atributos da classe carro
        self.modelo = modelo
        self.ano = ano
        self.quilometragem = quilometragem

    #método detalhes -> imprime as informações do carro
    def detalhes(self):
        return self.modelo, self.ano, self.quilometragem
    

#input do usuário
modeloCarro = str(input("Informe o modelo do carro: "))
anoCarro = int(input("Informe o ano do seu carro: "))
kmCarro = float(input("Informe a quilometragem do carro: "))

#instanciando a classe
meu_carro = Carro(modeloCarro, anoCarro, kmCarro)

#mostrando as informações do carro
modeloMeuCarro, anoMeuCarro, kmMeuCarro = meu_carro.detalhes()
print(f"O modelo do carro é: {modeloMeuCarro}\nO ano do carro é: {anoMeuCarro}\nA quilometragem do carro é {kmMeuCarro} km")
    