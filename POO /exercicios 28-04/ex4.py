""" 
4. Usar v_construtor corretamente
    Enunciado:
    Crie uma classe Filme cujo construtor receba v_titulo e v_duracao (v_construtores).
    Inicialize os atributos de instância titulo e duracao usando esses parâmetros.
"""

class Filme:      #classe criada 

    def __init__(self, v_titulo, v_duracao):    # Definindo v_construtores
        self.duracao = v_duracao
        self.titulo = v_titulo

# Inicializando os atributos de instancia 
filme1 = Filme("Velozes e Furiosos", 3)
filme2 = Filme("O massacre da Serra Elétrica", 2.30)

