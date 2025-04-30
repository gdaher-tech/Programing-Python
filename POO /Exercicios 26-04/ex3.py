"""
3. Crie uma classe Aluno com os atributos nome e nota.
Implemente dois métodos:

exibir_informacoes() → imprime o nome e a nota.
verificar_aprovacao() → imprime "Aprovado" se a nota for maior ou igual a 7, senão "Reprovado".
"""

class Aluno:    # Criação da classe 
    def __init__(self, nota : float, nome : str):
        self.nota = nota 
        self.nome = nome 
    
    def exibir_informacoes(self): 
        print(f"Aluno: {self.nome} | Nota: {self.nota}") 

    def verificar_aprovacao(self): 
        if self.nota >= 6: 
            print("Aprovado")
        else: 
            print("Reprovado")

nota = 5.4
nome = "Gustavo"

pessoa = Aluno(nota, nome)

pessoa.exibir_informacoes()

pessoa.verificar_aprovacao()

