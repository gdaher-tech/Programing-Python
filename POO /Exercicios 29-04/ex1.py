"""
Crie uma classe Livro com os atributos titulo e autor, 
e um método exibir_dados() que imprima essas informações.
"""

class Livro:     # Criando a classe Livro 

    # Criando os atributos no método construtor 
    def __init__(self, titulo, autor):
        self.titulo = titulo    # Titulo 
        self.autor = autor      # Autor 

    # Método da instância que mostra os valores dos atributos 
    def exibir_dados(self): 
        print(f"Titulo: {self.titulo} | Autor: {self.autor}")

# Criando a instância 
livro1 = Livro("O massacre da família Hope", "Harper Simons")

livro1.exibir_dados()

