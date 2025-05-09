class IntencaoDoar:
    """
    Classe que representa uma intenção de doação associada a um doador.

    Atributos:
        data_intencao (date): Data em que foi registrada a intenção de doar.
        status (str): Status da intenção (ex: Ativa, Cancelada, Confirmada).
    """

    banco_intencoes = {}

    def __init__(self, data_intencao, status="Ativa"):
        if not isinstance(status, str) or not status.strip():
            raise ValueError("Status inválido para a intenção de doar.")
        self.data_intencao = data_intencao
        self.status = status

    def registrar_intencao_doar(self, doador):
        """
        Registra a intenção de doar para o doador.
        """
        if doador.cpf in IntencaoDoar.banco_intencoes:
            raise ValueError("Este doador já possui uma intenção registrada.")
        
        IntencaoDoar.banco_intencoes[doador.cpf] = self
        doador.intencao_doar = self
        print(f"Intenção de doação registrada para o doador {doador._nome} (CPF: {doador.cpf}).")

    def atualizar_intencao_doar(self, nova_data=None, novo_status=None):
        """
        Atualiza a data e/ou o status da intenção de doar.
        """
        if nova_data is not None:
            self.data_intencao = nova_data
        if novo_status is not None:
            self.status = novo_status
        print("Intenção de doação atualizada com sucesso.")

    @property
    def status_atual(self):
        return self.status

    @property
    def data(self):
        return self.data_intencao
