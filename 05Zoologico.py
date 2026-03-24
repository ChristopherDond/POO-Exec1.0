class Animal:                           
    def fazer_som(self):
        print("Som genérico de animal.")  


class Cachorro(Animal):                 
    def fazer_som(self):
        print("Cachorro: Au au! 🐶")    


class Gato(Animal):
    def fazer_som(self):
        print("Gato: Miau! 🐱")


class Leao(Animal):
    def fazer_som(self):
        print("Leão: ROAAAAR! 🦁")

animais = [Cachorro(), Gato(), Leao(), Animal()]   

for animal in animais:                              
    animal.fazer_som()