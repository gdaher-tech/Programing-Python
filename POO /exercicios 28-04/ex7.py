"""
2. Adicionar um novo atributo depois da criação
    Enunciado:
    Crie uma classe ContaBancaria com atributos titular e saldo, recebidos no __init__.
    Após criar uma instância, adicione dinamicamente um atributo banco para essa instância, 
    e imprima todos os atributos dela.
"""


class ContaBancaria:    # Classe criada 

    def __init__(self, v_titular, v_saldo):     # Atributos construtores 
        self.titular = v_titular
        self.saldo = v_saldo

# Criando instancias 
conta1 = ContaBancaria("Anna", 2.580)
conta2 = ContaBancaria("Gustavo", 2.120)

conta2.banco = "Nubank"     # Adicionando atributo banco com valor definido

print(conta1.titular, conta1.saldo)     # Anna 2.58
print(conta2.titular, conta2.saldo, conta2.banco)   # Gustavo 2.12 Nubank