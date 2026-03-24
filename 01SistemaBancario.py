class ContaBancaria:
    def __init__(self, titular):        
        self.titular = titular          
        self.__saldo = 0.0              

    def depositar(self, valor):        
        if valor > 0:                   
            self.__saldo += valor       
            print(f"Depósito de R${valor:.2f} realizado.")
        else:
            print("Valor inválido. O depósito deve ser positivo.")

    def sacar(self, valor):             
        if valor > self.__saldo:        
            print("Saldo insuficiente.")
        elif valor <= 0:                
            print("Valor inválido.")
        else:
            self.__saldo -= valor       
            print(f"Saque de R${valor:.2f} realizado.")

    def ver_saldo(self):                
        return self.__saldo

conta = ContaBancaria("Christopher")
conta.depositar(500)
conta.sacar(200)
conta.sacar(400)        
print(conta.ver_saldo())