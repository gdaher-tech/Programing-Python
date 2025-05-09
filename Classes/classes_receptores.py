from .pessoa import Pessoa
from Utils.validadores import *

class Receptor(Pessoa):
    """
    Classe que representa um receptor no sistema.

    Atributos adicionais:
        orgao_necessario (str): Órgão necessário para o transplante.
        gravidade_condicao (str): Gravidade da condição do paciente.
        centro_transplante_vinculado (str): Nome do centro de transplante.
        contato_emergencia (str): Contato de emergência.
        posicao_lista_espera (str): Posição na lista de espera.
    """

    banco_receptores = {}

    def __init__(self, nome, idade, genero, data_nascimento, cidade_natal, estado_natal,
                 cpf, profissao, cidade_residencia, estado_residencia, estado_civil,
                 orgao_necessario, gravidade_condicao, centro_transplante_vinculado,
                 contato_emergencia, posicao_lista_espera):
        super().__init__(nome, idade, genero, data_nascimento, cidade_natal, estado_natal,
                         cpf, profissao, cidade_residencia, estado_residencia, estado_civil)

        self.orgao_necessario = orgao_necessario
        self.gravidade_condicao = gravidade_condicao
        self.centro_transplante_vinculado = centro_transplante_vinculado
        self.contato_emergencia = contato_emergencia
        self.posicao_lista_espera = posicao_lista_espera
        self.doacao = None

    def cadastrar(self):
        """
        Cadastra o receptor no banco de receptores.
        """
        if self.cpf in Receptor.banco_receptores:
            raise ValueError("CPF já cadastrado como receptor.")
        Receptor.banco_receptores[self.cpf] = self
        print("Receptor cadastrado com sucesso.")

    def editar(self, nome=None, idade=None, genero=None,
               cidade_residencia=None, estado_residencia=None,
               contato_emergencia=None, profissao=None):
        """
        Atualiza os dados gerais do receptor.
        """
        if nome is not None:
            self._nome = nome
        if idade is not None:
            self._idade = idade
        if genero is not None:
            self._genero = genero
        if cidade_residencia is not None:
            self._Pessoa__cidade_residencia = cidade_residencia
        if estado_residencia is not None:
            self._Pessoa__estado_residencia = estado_residencia
        if contato_emergencia is not None:
            self.contato_emergencia = contato_emergencia
        if profissao is not None:
            self._Pessoa__profissao = profissao
        print("Dados do receptor atualizados com sucesso.")

    def listar(self):
        """
        Retorna os dados do receptor em dicionário.
        """
        return {
            "id": self.id,
            "nome": self._nome,
            "idade": self._idade,
            "genero": self._genero,
            "data_nascimento": self._data_nascimento,
            "cidade_natal": self._cidade_natal,
            "estado_natal": self._estado_natal,
            "cpf": self.cpf,
            "profissao": self.profissao,
            "cidade_residencia": self.cidade_residencia,
            "estado_residencia": self.estado_residencia,
            "estado_civil": self._estado_civil,
            "orgao_necessario": self.orgao_necessario,
            "gravidade_condicao": self.gravidade_condicao,
            "centro_transplante_vinculado": self.centro_transplante_vinculado,
            "contato_emergencia": self.contato_emergencia,
            "posicao_lista_espera": self.posicao_lista_espera
        }

    def buscar(self, cpf):
        """
        Busca receptor pelo CPF.
        """
        return Receptor.banco_receptores.get(cpf)

    def excluir(self):
        """
        Remove receptor do banco.
        """
        if self.cpf in Receptor.banco_receptores:
            del Receptor.banco_receptores[self.cpf]
            print("Receptor excluído com sucesso.")
        else:
            print("Receptor não encontrado.")

    def atualizar_situacao_receptor(self, orgao_necessario=None, gravidade_condicao=None, posicao_lista_espera=None):
        """
        Atualiza informações médicas do receptor.
        """
        if orgao_necessario is not None:
            self.orgao_necessario = orgao_necessario
        if gravidade_condicao is not None:
            self.gravidade_condicao = gravidade_condicao
        if posicao_lista_espera is not None:
            self.posicao_lista_espera = posicao_lista_espera
        print("Situação médica do receptor atualizada com sucesso.")

    def associar_doacao(self, doacao):
        """
        Associa uma doação a este receptor.
        """
        if self.doacao is not None:
            raise ValueError("Este receptor já possui uma doação associada.")
        self.doacao = doacao
        print("Doação associada ao receptor com sucesso.")
