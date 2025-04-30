"""
2. Crie uma classe ContaCorrente com os atributos titular e saldo.
Implemente dois métodos:

depositar(valor)
consultar_saldo()
"""

class ContaCorrente:    # Criando a classe
    def __init__(self, titular, saldo):
        self.titular = titular 
        self.saldo = saldo
    
    def depositar(self, saldo): 
        self.saldo += saldo 

    def consultar_saldo(self): 
        return self.saldo

# Criando a instância
pessoa1 = ContaCorrente("Gustavo", 0)

# Depostitando 
pessoa1.depositar(50)

# Consultando Saldo 
print(pessoa1.consultar_saldo())