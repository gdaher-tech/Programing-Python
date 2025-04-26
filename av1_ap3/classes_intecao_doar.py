class IntencaoDoar:
    """
    Classe que representa uma intenção de doação associada a um doador.

    Atributos:
        data_intencao (str): Data em que foi registrada a intenção de doar.
        status (str): Status da intenção (ex: Ativa, Cancelada, Confirmada).

    Métodos:
        registrar_intencao_doar(): Registra a intenção de doar.
        atualizar_intencao_doar(): Atualiza data e/ou status da intenção.
    """

    banco_intencoes = {}

    def __init__(self, data_intencao, status="Ativa"):
        self.data_intencao = data_intencao
        self.status = status

    def registrar_intencao_doar(self, doador):
        """
        Registra a intenção de doar para o doador.
        """
        if doador.cpf in IntencaoDoar.banco_intencoes:
            raise ValueError("Este doador já possui uma intenção registrada.")
        
        IntencaoDoar.banco_intencoes[doador.cpf] = self
        doador.intencao_doar = self  # Associa diretamente no doador
        print("Intenção de doar registrada com sucesso.")

    def atualizar_intencao_doar(self, nova_data=None, novo_status=None):
        """
        Atualiza a data e/ou o status da intenção de doar.
        """
        if nova_data is not None:
            self.data_intencao = nova_data
        if novo_status is not None:
            self.status = novo_status
        print("Intenção de doação atualizada com sucesso.")
