"""
5. Método para alterar atributo de instância
Enunciado:
Crie uma classe Aluno que receba nome e nota no __init__.
Crie um método atualizar_nota(nova_nota) que permita alterar a nota depois da criação.

Teste criando um aluno, alterando a nota e imprimindo antes e depois.
"""

class Aluno: 
    def __init__(self, nome = 'Gustavo'):
        self.nome = nome 
        self.nota = 8.2 

def atualizar_nota(self): 
    nova_nota = 8.9
    self.nota = nova_nota
aluno1 = Aluno()

print(aluno1.nota)

atualizar_nota(aluno1)

print(aluno1.nota)