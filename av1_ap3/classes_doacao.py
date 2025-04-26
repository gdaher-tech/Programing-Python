from uuid import uuid4

class Doacao:
    """
    Classe que representa uma intenção de doação no sistema.

    Atributos:
        id (str): Identificador único da doação.
        data_doacao (str): Data prevista para a doação.
        status (str): Status da intenção de doação (ex: Aguardando, Confirmado, Cancelado).

    Métodos:
        registrar_intencao_doar(): Registra a intenção de doar no banco de doações.
        atualizar_intencao_doar(): Atualiza o status ou a data da doação.
    """

    banco_doacoes = {}

    def __init__(self, data_doacao, status="Aguardando"):
        self.id = str(uuid4())  # Gera um ID único para a doação
        self.data_doacao = data_doacao
        self.status = status
        self.receptor = None  # Pode ou não ter um receptor associado
        

    def registrar_intencao_doar(self):
        """
        Registra a doação no banco de doações.

        Exemplo:
            doacao.registrar_intencao_doar()
        """
        if self.id in Doacao.banco_doacoes:
            raise ValueError("Doação já registrada.")
        Doacao.banco_doacoes[self.id] = self
        print(f"Intenção de doação registrada com sucesso! ID: {self.id}")

    def atualizar_intencao_doar(self, nova_data=None, novo_status=None):
        """
        Atualiza a data prevista e/ou o status da doação.

        Parâmetros:
            nova_data (str): Nova data da doação (opcional).
            novo_status (str): Novo status da doação (opcional).

        Exemplo:
            doacao.atualizar_intencao_doar(novo_status="Confirmado")
        """
        if nova_data is not None:
            self.data_doacao = nova_data
        if novo_status is not None:
            self.status = novo_status
        print("Intenção de doação atualizada com sucesso.")

    def associar_receptor(self, receptor):
        """
        Associa um receptor a esta doação.
        """
        if self.receptor is not None:
            raise ValueError("Esta doação já possui um receptor associado.")
        self.receptor = receptor
        print("Receptor associado à doação com sucesso.")

