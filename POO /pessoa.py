class Pessoa:
    # Inicializador que recebe o valor do objeto vindo de fora da classe  
    def __init__(self, nome, sobrenome):

        # Objeto |      # Atributo
        self.nome =     nome 
        self.sobrenome = sobrenome 

    def unir_nome(self): 
        self.nome_completo = self.nome + self.sobrenome
        print(f"Nome completo: {self.nome_completo}")

    
nome = "Gustavo"
sobrenome = "Daher"

pessoa = Pessoa(nome, sobrenome) 

pessoa.unir_nome()
        