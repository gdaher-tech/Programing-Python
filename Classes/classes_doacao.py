from uuid import uuid4

class Doacao:
    """
    Classe que representa uma doação no sistema.

    Atributos:
        id (str): Identificador único da doação.
        data_doacao (date): Data prevista para a doação.
        status (str): Status da doação (ex: Aguardando, Confirmado, Cancelado).
        receptor (Receptor | None): Receptor associado à doação.
    """

    banco_doacoes = {}

    def __init__(self, data_doacao, status="Aguardando"):
        if not isinstance(status, str) or not status.strip():
            raise ValueError("Status inválido.")
        self.id = str(uuid4())
        self.data_doacao = data_doacao
        self.status = status
        self.receptor = None

    def registrar_intencao_doar(self):
        """
        Registra a doação no banco de dados.
        """
        if self.id in Doacao.banco_doacoes:
            raise ValueError(f"A doação com ID {self.id} já foi registrada.")
        Doacao.banco_doacoes[self.id] = self
        print(f"✅ Doação registrada com sucesso! ID: {self.id}")

    def atualizar_intencao_doar(self, nova_data=None, novo_status=None):
        """
        Atualiza a data prevista e/ou o status da doação.
        """
        if nova_data is not None:
            self.data_doacao = nova_data
        if novo_status is not None:
            self.status = novo_status
        print("✅ Intenção de doação atualizada com sucesso.")

    def associar_receptor(self, receptor):
        """
        Associa um receptor a esta doação.
        """
        if self.receptor is not None:
            raise ValueError("❌ Esta doação já possui um receptor associado.")
        self.receptor = receptor
        print(f"✅ Receptor {receptor._nome} associado à doação com sucesso.")

    @property
    def resumo(self):
        """
        Retorna um resumo da doação.
        """
        return {
            "id": self.id,
            "data": self.data_doacao,
            "status": self.status,
            "receptor": self.receptor.cpf if self.receptor else "Nenhum"
        }
