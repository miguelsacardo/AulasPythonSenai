#crie uma classe Circulo com um atributo raio e um método area() para calcular a área do circulo

class Circulo:

    def __init__(self, raio):
        self.raio = raio

    #método area() para calcular a área do circulo
    def area(self):
        area = 3.14 * self.raio**2
        return area

area_circulo = Circulo(5)
print(f"A área do circulo que possui 5 de raio é {area_circulo.area()}")
