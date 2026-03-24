class Funcionario:                          
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def mostrar_dados(self):                
        print(f"Nome: {self.nome} | Salário: R${self.salario:.2f}")

class Gerente(Funcionario):                 
    def __init__(self, nome, salario, bonus):
        super().__init__(nome, salario)     
        self.bonus = bonus

    def calcular_salario_total(self):       
        return self.salario + self.bonus


class Desenvolvedor(Funcionario):           
    def __init__(self, nome, salario, linguagem):
        super().__init__(nome, salario)
        self.linguagem = linguagem

    def programar(self):                    
        print(f"{self.nome} está programando em {self.linguagem}.")


class Estagiario(Funcionario):              
    def __init__(self, nome, salario, carga_horaria):
        super().__init__(nome, salario)
        self.carga_horaria = carga_horaria

    def estudar(self):                      
        print(f"{self.nome} estuda {self.carga_horaria}h por semana.")

g = Gerente("Ana", 8000, 2000)
g.mostrar_dados()
print(f"Salário total: R${g.calcular_salario_total():.2f}")

d = Desenvolvedor("Carlos", 6000, "Python")
d.mostrar_dados()
d.programar()

e = Estagiario("Lucas", 1500, 20)
e.mostrar_dados()
e.estudar()