"""
Usuario
Crie uma classe Usuario com nome e senha.
Implemente um método verificar_senha(senha_digitada) que retorna True ou False.
"""


class Usuario: 

    def __init__(self, nome, senha):
        self.nome = nome 
        self.senha = senha 
    
    def verificar_senha(self, senha_digitada): 
        if self.senha == senha_digitada: 
            return True
        else: 
            return False
    
user_gustavodh = Usuario(nome = input("Insira o seu nome e sobrenome \n"), 
                         senha = input("Escolha a senha para sua conta \n"))



user_gustavodh.verificar_senha(senha_digitada = input("Digite a senha para acessar a sua conta \n"))

