"""
Crie uma classe Carro com atributos modelo, ano.
Adicione um método idade_carro(ano_atual) que retorna a idade do carro
"""

from datetime import datetime   # Importando biblioteca para extrair o ano atual 



class Carro: 
    def __init__(self, modelo, ano):
        self.modelo = modelo 
        self.ano = ano 

    def idade_carro(self): 
        idade_carro = datetime.now().year - self.ano
        print(f"O carro tem {idade_carro} anos")


fusca_ssp9c62 = Carro("Fusca", 1987)

fusca_ssp9c62.idade_carro()