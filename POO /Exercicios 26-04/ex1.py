"""
1. Crie uma classe Livro com os atributos titulo e autor.
Depois, crie um método descricao() que imprime:
"Título: <titulo> | Autor: <autor>"
"""

class Livro:    #Criando a classe livro 
    def __init__(self, titulo, autor):
        self.titulo = titulo       
        self.autor = autor 

    def descricao(self): 
        print(f"Título: {self.titulo} | Autor: {self.autor}")

livro1 = Livro("Python Eficaz", "Gustavo")    # Criando Instancia, passando os valores dos atributos 

livro1.descricao()  # Ativando a funcao descricao pelo objeto 

    