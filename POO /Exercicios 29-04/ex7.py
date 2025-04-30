"""
Celular
Crie uma classe Celular com o atributo bateria.
Implemente usar_bateria(tempo) que reduz a bateria em 10% por hora usada.
"""

class Celular: 
    
    def __init__(self, bateria):
        self.bateria = bateria 
        
    def usar_bateria(self, tempo):
        self.bateria = self.bateria - (tempo * 10)
        print(f"Bateria esta em {self.bateria}%")

android_user49 = Celular(100)

android_user49.usar_bateria(tempo = int(input("Por quanto tempo usou o celular? (em horas sem usar letras) \n")))

print(android_user49.usar_bateria)

