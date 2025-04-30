"""
Funcionario
Crie uma classe Funcionario com nome e salario.
Implemente um método aumentar_salario(percentual).
"""

class Funcionario: 

    def __init__(self, nome, salario):

        self.nome = nome 
        self.salario = salario

    def aumentar_salario(self, porcentagem_aumento): 
        self.salario = self.salario + (self.salario * porcentagem_aumento / 100)


gerente_pedro = Funcionario("Pedro Henrique", 2500)

gerente_pedro.aumentar_salario(porcentagem_aumento = int(input("Insira a porcentagem de aumento (sem utilizar %) \n")))

print(gerente_pedro.salario)