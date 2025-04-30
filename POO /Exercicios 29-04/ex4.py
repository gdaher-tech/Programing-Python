"""
Crie uma classe Produto com atributos nome, preco.
Implemente um método aplicar_desconto(porcentagem).
"""

class Produto: 

    def __init__(self, nome, preco):
        self.nome = nome 
        self.preco = preco

    def aplicar_desconto(self, percentual_decimal):
        self.preco = self.preco - (self.preco * percentual_decimal)

produto_1 = Produto("Garrafa Térmica", 180)


print(produto_1.aplicar_desconto(percentual_decimal = 15))