"""
Crie uma classe Conta com atributos titular e saldo.
Implemente um método sacar(valor) que subtrai do saldo se houver saldo suficiente.
"""

class Conta:    # Criando a classe conta 

    def __init__(self, titular : str, saldo : float):
        self.titular = titular 
        self.saldo = saldo 
    
    def sacar(self, saque):     # Criando 
        if saque <= self.saldo:
            self.saldo = self.saldo - saque
            print(f"SALDO ATUAL: {self.saldo}") 
        
        elif saque > self.saldo: 
            print("SEM SALDO O SUFICIENTE PARA SAQUE")

# Criando instancia 
conta01 = Conta("Gustavo Garcia", 2850)

# Aplicando método de instancia 
conta01.sacar(500)

