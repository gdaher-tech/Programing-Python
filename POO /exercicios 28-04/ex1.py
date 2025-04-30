""""
1. Criação de atributos via __init__
Enunciado:
Crie uma classe Livro que tenha atributos titulo e autor, ambos recebidos pelo construtor.
Depois, crie duas instâncias de Livro com valores diferentes e imprima seus atributos.
"""

class Livro:    # Classe livro criada 

    def __init__(self, titulo, autor):      # Atributos recebidos pelo construtor
        self.titulo = titulo 
        self.autor = autor 

# Criando instancias de Livro com valores diferentes 
livro1 = Livro("Nunca Minta", "Freida Mc Fadein")
livro2 = Livro("O Massacre da família Hope", "Riley Sager")     

# Imprimindo os seus atributos 
print(livro1.autor, livro1.titulo)  # Freida Mc Fadein Nunca Minta
print(livro2.autor, livro2.titulo)  # Riley Sager O Massacre da família Hope




