class Pessoa:   # Criação da classe

    def __init__(self, nome, idade):    # Parâmetros contrutores 
        # Atributos da instância 
        self.nome = nome 
        self.idade = idade 

    # Método da classe
    @classmethod 
    def criar_bebe(cls, nome): 
        return cls(nome, 0) # Cria uma pessoa com a idade 0 
    
# Criando as instâncias 
p1 = Pessoa("Lucas", 25)    # Criação de instância da maneira convencional 
p2 = Pessoa.criar_bebe("Bebê João")     # Factory method 

