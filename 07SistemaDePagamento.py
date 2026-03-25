from abc import ABC, abstractmethod

class Pagamento(ABC):
    @abstractmethod
    def pagar(self, valor):
        pass      

class Cartao(Pagamento):
    def pagar(self, valor):
        print(f"💳 Pagamento de R${valor:.2f} via Cartão aprovado.")


class Pix(Pagamento):
    def pagar(self, valor):
        print(f"⚡ Pix de R${valor:.2f} enviado instantaneamente.")


class Boleto(Pagamento):
    def pagar(self, valor):
        print(f"📄 Boleto de R${valor:.2f} gerado. Vence em 3 dias.")

pagamentos = [Cartao(), Pix(), Boleto()]

for p in pagamentos:
    p.pagar(199.90)