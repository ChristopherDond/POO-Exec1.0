from abc import ABC, abstractmethod

class Transporte(ABC):
    @abstractmethod
    def mover(self):
        pass

class Carro(Transporte):
    def mover(self):
        print("🚗 Carro se move pelas ruas da cidade.")


class Aviao(Transporte):
    def mover(self):
        print("✈️  Avião decola e cruza o céu a 900km/h.")


class Barco(Transporte):
    def mover(self):
        print("🚢 Barco navega pelo oceano silenciosamente.")

transportes = [Carro(), Aviao(), Barco()]

for t in transportes:
    t.mover()