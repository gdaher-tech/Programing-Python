"""
4. Crie uma classe Carro que tenha os atributos modelo e ano.
Implemente um método exibir_dados() que apenas lê (sem modificar) os atributos.
"""

class Carro: 
    def __init__(self, modelo, ano):
        self.modelo = modelo 
        self.ano = ano
    
    def exibir_dados(self): 
        print(f"Modelo {self.modelo} | Ano {self.ano}")
    
amarok = Carro("Amarok Highline V6", 2022)

amarok.exibir_dados()
