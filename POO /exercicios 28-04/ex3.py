"""
3. Criar atributo de classe
    Enunciado:
    Crie uma classe Animal com o atributo de classe reino = "Animalia".
    Depois, crie duas instâncias e mostre que ambas possuem o atributo reino.
"""

class Animal:   # classe criada 

    reino = "animalia"      # Atributo de classe criado

    def __init__(self):
        pass

# Criando instancias 
animal1 = Animal()
animal2 = Animal()

print(animal1.reino)    # animalia
print(animal2.reino)    # animalia