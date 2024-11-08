'''1. Classe Triângulo. Crie uma classe Triangulo com atributos base e altura.
 Adicione o método area() para calcular a área do triângulo.'''

class Triangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura =altura

    #função que calcula a área do triângulo
    def area(self):
        areaTriangulo = self.base * self.altura / 2
        return areaTriangulo
    
#input do usuário
baseTriangulo = float(input("Digite o valor da base do triângulo: "))
alturaTriangulo = float(input("DIgite o valor da altura do triângulo: "))

#instanciando a classe
areaT = Triangulo(baseTriangulo,alturaTriangulo)

#mostrando a área
print(f"A área do triângulo de base {baseTriangulo} e altura {alturaTriangulo} é {areaT.area()}")
