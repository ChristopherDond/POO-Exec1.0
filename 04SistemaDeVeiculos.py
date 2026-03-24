class Veiculo:                         
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def mover(self):                   
        print(f"{self.marca} {self.modelo} está se movendo.")


class Carro(Veiculo):                  
    def abrir_porta_malas(self):
        print(f"Porta-malas do {self.modelo} aberto.")


class Moto(Veiculo):                    
    def empinar(self):
        print(f"{self.modelo} empinando! 🏍️")


class Caminhao(Veiculo):             
    def carregar_carga(self):
        print(f"{self.modelo} carregando carga pesada.")

c = Carro("Toyota", "Corolla")
c.mover()                   
c.abrir_porta_malas()      

m = Moto("Honda", "CB 500")
m.mover()
m.empinar()

cam = Caminhao("Volvo", "FH")
cam.mover()
cam.carregar_carga()