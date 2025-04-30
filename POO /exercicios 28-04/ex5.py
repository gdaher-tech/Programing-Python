"""
5. Modificar o atributo de uma instância sem afetar outra
Enunciado:
Crie uma classe Computador que receba marca e memoria pelo construtor.
Crie duas instâncias: altere a memoria de uma delas depois de criada.
Mostre que a outra instância não foi alterada.
"""

class Computador: 

    def __init__(self, v_marca, v_memoria):
        self.marca = v_marca
        self.memoria = v_memoria

# Criando as intancias 

pc1 = Computador("Asus", "86gb")
pc2 = Computador("Apple", "128gb")

pc1.memoria = "128gb"

print(pc1.memoria, pc1.marca)
print(pc2.memoria, pc2.marca)