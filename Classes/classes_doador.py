from .pessoa import Pessoa
from Utils.validadores import *

class Doador(Pessoa):
    """
    Classe que representa um doador no sistema.

    Atributos adicionais:
        tipo_sanguineo (str): Tipo sanguíneo do doador.
        contato_emergencia (str): Contato de emergência.
        intencao_doar (IntencaoDoar | None): Intenção de doar associada ao doador (opcional).
        doacao (Doacao | None): Doação efetivada associada ao doador (opcional).
    """

    banco_doador = {}

    def __init__(self, nome, idade, genero, data_nascimento, cidade_natal, estado_natal,
                 cpf, profissao, cidade_residencia, estado_residencia, estado_civil,
                 tipo_sanguineo, contato_emergencia):
        super().__init__(nome, idade, genero, data_nascimento, cidade_natal, estado_natal,
                         cpf, profissao, cidade_residencia, estado_residencia, estado_civil)

        self._tipo_sanguineo = tipo_sanguineo
        self._contato_emergencia = contato_emergencia
        self.intencao_doar = None
        self.doacao = None

    def cadastrar(self):
        """
        Cadastra o doador após validações.
        """
        validar_nome(self._nome)
        validar_idade(self._idade)
        validar_genero(self._genero)
        validar_dataNascimento(self._data_nascimento)
        validar_cidadeNatal(self._cidade_natal)
        validar_estadoNatal(self._estado_natal)
        validar_cpf(self.cpf)
        validar_profissao(self.profissao)
        validar_cidadeResidencia(self.cidade_residencia)
        validar_estadoResidencia(self.estado_residencia)
        validar_estadoCivil(self._estado_civil)

        if not isinstance(self._tipo_sanguineo, str) or not self._tipo_sanguineo.strip():
            raise ValueError("Tipo sanguíneo inválido.")
        if not isinstance(self._contato_emergencia, str) or not self._contato_emergencia.strip():
            raise ValueError("Contato de emergência inválido.")

        if self.cpf in Doador.banco_doador:
            raise ValueError("CPF já cadastrado como doador.")

        Doador.banco_doador[self.cpf] = self
        print("Doador cadastrado com sucesso.")

    def editar(self, nome=None, idade=None, genero=None, data_nascimento=None,
               cidade_natal=None, estado_natal=None, cpf=None, profissao=None,
               cidade_residencia=None, estado_residencia=None, estado_civil=None,
               tipo_sanguineo=None, contato_emergencia=None):
        """
        Edita os dados do doador.
        """
        if nome is not None:
            self._nome = nome
        if idade is not None:
            self._idade = idade
        if genero is not None:
            self._genero = genero
        if data_nascimento is not None:
            self._data_nascimento = data_nascimento
        if cidade_natal is not None:
            self._cidade_natal = cidade_natal
        if estado_natal is not None:
            self._estado_natal = estado_natal
        if profissao is not None:
            self._profissao = profissao
        if cidade_residencia is not None:
            self._cidade_residencia = cidade_residencia
        if estado_residencia is not None:
            self._estado_residencia = estado_residencia
        if estado_civil is not None:
            self._estado_civil = estado_civil
        if tipo_sanguineo is not None:
            self._tipo_sanguineo = tipo_sanguineo
        if contato_emergencia is not None:
            self._contato_emergencia = contato_emergencia
        print("Dados do doador atualizados com sucesso.")

    def listar(self):
        """
        Retorna os dados do doador em formato de dicionário.
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
            "tipo_sanguineo": self._tipo_sanguineo,
            "contato_emergencia": self._contato_emergencia
        }

    def buscar(self, cpf):
        """
        Busca o doador pelo CPF no banco de doadores.
        """
        return Doador.banco_doador.get(cpf)

    def excluir(self):
        """
        Exclui o doador do banco de dados usando o CPF.
        """
        if self.cpf in Doador.banco_doador:
            del Doador.banco_doador[self.cpf]
            print("Doador excluído com sucesso.")
        else:
            print("Doador não encontrado.")
