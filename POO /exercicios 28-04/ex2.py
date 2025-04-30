"""
2. Definir atributo fixo sem parâmetro no __init__
Enunciado:
Crie uma classe Pais que tenha o atributo continente fixado como "América do Sul" dentro do __init__, sem recebê-lo como parâmetro.
Crie uma instância e mostre o valor de continente.
"""

class Pais:     # Classe criada  
    
    def __init__(self):     # Não passo continente como parametro 
        self.continente = "América do Sul"      # Defino continente com o valor especifiicado como fixo do atributo 

# Criando a instancia 
pais1 = Pais()

print(pais1.continente) # América do Sul

    
