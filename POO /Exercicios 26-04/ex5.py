"""
5. Crie uma classe ConfiguracaoSistema com o atributo modo_escuro (booleano).
Crie um método ativar_modo_escuro() que altera modo_escuro para True.
"""

class ConfiguracoesSistema: 
    def __init__(self, modo_escuro):
        self.modo_escuro = modo_escuro 

    def ativar_modo_escuro(self): 
        self.modo_escuro = True 
        print("Modo escuro ativado")
    
sistema = ConfiguracoesSistema(modo_escuro = False)

sistema.ativar_modo_escuro()