"""
3. Definir atributo fixo e recebido
Enunciado:
Crie uma classe Celular que tenha:

Um atributo fixo sistema_operacional = "Android"
E receba modelo e preco via __init__.
Crie duas instâncias e imprima seus dados.
"""

class Celular:  # Classe criada 
    def __init__(self, v_modelo, v_preco):      # v_construtores 
        self.sistema_operacional = "Android"    # Atributo fixo 
        self.modelo = v_modelo
        self.preco = v_preco

# Instancias 
cel1 = Celular("A21", 960.00)
cel2 = Celular("S25 Ultra", 3.480)


print(cel1.modelo, cel1.preco, cel1.sistema_operacional)    # A21 960.0 Android
print(cel2.modelo, cel2.preco, cel2.sistema_operacional)    # S25 Ultra 3.48 Android

