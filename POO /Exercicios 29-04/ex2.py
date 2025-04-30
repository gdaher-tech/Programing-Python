"""
Crie uma classe Aluno com atributos nome e nota.
Adicione um método verificar_aprovacao() que imprime "Aprovado" se nota ≥ 7.
"""

class Aluno:    # Classe criada 
    
    def __init__(self, nome, nota : float):
        self.nome = nome 
        self.nota = nota 

    def verificar_aprovacao(self): 
        if self.nota >= 7: 
            print(f"{self.nome} Aprovado")


aluno1 = Aluno(None, None)    # Cria a instacia 

aluno1.nome = input("Qual o nome do Aluno? ")   # Atribui o nome ao objeto aluno1 
aluno1.nota = float(input("Qual a nota do Aluno? "))   # Atribui uma nota ao objeto aluno1

aluno1.verificar_aprovacao()    # Chama o método de classe que verifica a aprovação do aluno 