"""
1. Alterar atributo de classe apenas para uma instância
    Enunciado:
    Crie uma classe Empresa com um atributo de classe pais = "Brasil".
    Crie duas instâncias.
    Altere o pais apenas para uma instância.
    Mostre que o atributo da outra instância e da classe não mudaram.
"""

class Empresa:  # Classe

    pais = "Brasil"     # Atributo de classe 

    def __init__(self):
        pass

# Criando instancia 
empresa1 = Empresa()
empresa2 = Empresa()

empresa1.pais = "Indonésia"     # Alterando o atributo pais somente para a empresa 1 

# Imprimindo os resultados 
print(empresa1.pais)    # Indonésia
print(empresa2.pais)    # Brasil 


