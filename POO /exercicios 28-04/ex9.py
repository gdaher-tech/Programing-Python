"""
Exercício 4 (faltando): Definir valores padrão no __init__
Enunciado:

Crie uma classe Produto que tenha nome e preco, mas defina valores padrão no __init__.
Ou seja: se o usuário não passar nada, o produto vira "Sem Nome" e 0.0.
"""

class Produto: 

    def __init__(self):
        self.nome = "Sem Nome"
        self.preco = 0.0

p1 = Produto()
print(p1.nome, p1.preco)