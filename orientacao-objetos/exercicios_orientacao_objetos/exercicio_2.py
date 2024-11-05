#crie uma classe Retangulo com atributos altura e largura e um método perimetro() para calcular o perímetro

class Retangulo:
    def __init__(self, altura,largura):
        self.altura = altura
        self.largura = largura

    def perimetro(self):
        perimetro = (self.altura * 2) + (self.largura * 2)
        return perimetro


perimetro_retangulo = Retangulo(2,5)
print(f"O perímetro de um retâmgulo com 2 de altura e 5 de largura é {perimetro_retangulo.perimetro()}")