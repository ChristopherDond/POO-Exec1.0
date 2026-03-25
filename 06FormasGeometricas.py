import math

class Forma:
    def calcular_area(self):
        return 0

class Quadrado(Forma):
    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):
        return self.lado ** 2

class Retangulo(Forma):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def calcular_area(self):
        return self.largura * self.altura

class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
        return math.pi * self.raio ** 2

formas = [Quadrado(4), Retangulo(3, 5), Circulo(7)]

for forma in formas:
    print(f"{forma.__class__.__name__}: área = {forma.calcular_area():.2f}")