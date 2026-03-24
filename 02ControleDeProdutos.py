class Produto:
    def __init__(self, nome, preco):     
        self.nome = nome                 
        self.__preco = 0.0               
        self.__definir_preco(preco)      

    def __definir_preco(self, valor):    
        if valor >= 0:
            self.__preco = valor
        else:
            print("Preço inválido. Mantendo R$0.00.")

    def aplicar_desconto(self, percentual):   
        if 0 < percentual < 100:
            self.__preco -= self.__preco * (percentual / 100)
            print(f"Desconto de {percentual}% aplicado.")
        else:
            print("Percentual inválido. Use valores entre 0 e 100.")

    def aumentar_preco(self, percentual):     
        if percentual > 0:
            self.__preco += self.__preco * (percentual / 100)
            print(f"Preço aumentado em {percentual}%.")
        else:
            print("Percentual inválido.")

    def mostrar_preco(self):                  
        print(f"{self.nome}: R${self.__preco:.2f}")

