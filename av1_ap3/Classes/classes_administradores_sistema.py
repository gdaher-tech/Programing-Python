from .pessoa import Pessoa
from Utils.validadores import *
from .classes_doador import Doador
from datetime import date


class AdministradorSistema(Pessoa):
    """
    Classe que representa um administrador do sistema.

    Atributos:
        nome_usuario (str): Nome de login do administrador.
        senha (str): Senha do administrador.

    Métodos:
        cadastrar, editar, listar, buscar, excluir (obrigatórios da Pessoa)
        login, logout, recuperar_senha
        gerenciar_pessoas, gerenciar_orgaos, gerenciar_tipos_de_orgao, gerenciar_centros_distribuicao
    """

    banco_administradores = {}
    banco_orgaos = {}   # Implementar tipo de orgao junto 
    banco_tipos_orgao = {}
    banco_centros_distribuicao = {}

    def __init__(self, nome, idade, genero, data_nascimento, cidade_natal, estado_natal,
                 cpf, profissao, cidade_residencia, estado_residencia, estado_civil,
                 nome_usuario, senha):
        super().__init__(nome, idade, genero, data_nascimento, cidade_natal, estado_natal,
                         cpf, profissao, cidade_residencia, estado_residencia, estado_civil)
        self.nome_usuario = nome_usuario
        self.senha = senha

    @property
    def cpf(self):
        return self._Pessoa__cpf

    ## Métodos obrigatórios de Pessoa
    def cadastrar(self):
        if self.nome_usuario in AdministradorSistema.banco_administradores:
            raise ValueError("Usuário já cadastrado.")
        AdministradorSistema.banco_administradores[self.nome_usuario] = self
        print("Administrador cadastrado com sucesso.")

    def editar(self, nome_usuario=None, senha=None):
        if nome_usuario is not None:
            self.nome_usuario = nome_usuario
        if senha is not None:
            self.senha = senha
        print("Administrador atualizado com sucesso.")

    def listar(self):
        return {
            "id": self._Pessoa__id,
            "nome": self._nome,
            "idade": self._idade,
            "genero": self._genero,
            "data_nascimento": self._data_nascimento,
            "cidade_natal": self._cidade_natal,
            "estado_natal": self._estado_natal,
            "cpf": self._Pessoa__cpf,
            "profissao": self._Pessoa__profissao,
            "cidade_residencia": self._Pessoa__cidade_residencia,
            "estado_residencia": self._Pessoa__estado_residencia,
            "estado_civil": self._estado_civil,
            "nome_usuario": self.nome_usuario
        }

    def buscar(self, nome_usuario):
        return AdministradorSistema.banco_administradores.get(nome_usuario)

    def excluir(self):
        if self.nome_usuario in AdministradorSistema.banco_administradores:
            del AdministradorSistema.banco_administradores[self.nome_usuario]
            print("Administrador excluído com sucesso.")
        else:
            print("Administrador não encontrado.")

    ## Métodos de login/logout/recuperação
    def login(self, nome_usuario, senha):
        if nome_usuario in AdministradorSistema.banco_administradores:
            admin = AdministradorSistema.banco_administradores[nome_usuario]
            if admin.senha == senha:
                print("Login realizado com sucesso!")
            else:
                raise ValueError("Senha incorreta!")
        else:
            raise ValueError("Usuário não encontrado!")

    def logout(self):
        print("Logout realizado com sucesso.")

    def recuperar_senha(self, nome_usuario, nova_senha):
        if nome_usuario in AdministradorSistema.banco_administradores:
            admin = AdministradorSistema.banco_administradores[nome_usuario]
            admin.senha = nova_senha
            print("Senha atualizada com sucesso!")
        else:
            raise ValueError("Usuário não encontrado!")

    ## Métodos de gerenciamento
    def gerenciar_pessoas(self):
        while True:
            print("\n--- Gerenciamento de Pessoas ---")
            print("1. Cadastrar novo doador")
            print("2. Listar doadores")
            print("3. Voltar")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                print("\n--- Cadastro de Novo Doador ---")
                nome = input("Nome: ")
                idade = int(input("Idade: "))
                genero = input("Gênero: ")
                data_nascimento = input("Data de nascimento (AAAA-MM-DD): ")
                cidade_natal = input("Cidade natal: ")
                estado_natal = input("Estado natal: ")
                cpf = input("CPF (somente números): ")
                profissao = input("Profissão: ")
                cidade_residencia = input("Cidade de residência: ")
                estado_residencia = input("Estado de residência: ")
                estado_civil = input("Estado civil (solteiro/casado/viuvo/uniao estavel): ")
                tipo_sanguineo = input("Tipo sanguíneo: ")
                contato_emergencia = input("Contato de emergência: ")

                novo_doador = Doador(
                    nome, idade, genero, date(data_nascimento), cidade_natal, estado_natal,
                    cpf, profissao, cidade_residencia, estado_residencia, estado_civil,
                    tipo_sanguineo, contato_emergencia
                )

                novo_doador.cadastrar()
                print("Doador cadastrado com sucesso!")
            elif opcao == "2":
                print("\n--- Lista de Doadores ---")
                for cpf, doador in Doador.banco_doador.items():
                    print(doador.listar())

            elif opcao == "3":
                print("Voltando ao menu principal...")
                break
            else:
                print("Opção inválida.")

    def gerenciar_orgaos(self):
        while True:
            print("\n--- Gerenciamento de Órgãos ---")
            print("1. Cadastrar novo órgão")
            print("2. Listar órgãos")
            print("3. Voltar")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                nome_orgao = input("Nome do órgão: ")
                tipo = input("Tipo do órgão: ")
                AdministradorSistema.banco_orgaos[nome_orgao] = tipo
                print("Órgão cadastrado com sucesso.")

            elif opcao == "2":
                for nome, tipo in AdministradorSistema.banco_orgaos.items():
                    print(f"Órgão: {nome} | Tipo: {tipo}")

            elif opcao == "3":
                print("Voltando ao menu principal...")
                break
            else:
                print("Opção inválida.")

    def gerenciar_tipos_de_orgao(self):
        while True:
            print("\n--- Gerenciamento de Tipos de Órgãos ---")
            print("1. Cadastrar novo tipo")
            print("2. Listar tipos")
            print("3. Voltar")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                tipo = input("Nome do novo tipo de órgão: ")
                AdministradorSistema.banco_tipos_orgao[tipo] = True
                print("Tipo cadastrado com sucesso.")

            elif opcao == "2":
                for tipo in AdministradorSistema.banco_tipos_orgao:
                    print(f"Tipo de órgão: {tipo}")

            elif opcao == "3":
                print("Voltando ao menu principal...")
                break
            else:
                print("Opção inválida.")

    def gerenciar_centros_distribuicao(self):
        while True:
            print("\n--- Gerenciamento de Centros de Distribuição ---")
            print("1. Cadastrar novo centro")
            print("2. Listar centros")
            print("3. Voltar")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                nome_centro = input("Nome do centro: ")
                endereco = input("Endereço do centro: ")
                AdministradorSistema.banco_centros_distribuicao[nome_centro] = endereco
                print("Centro cadastrado com sucesso.")

            elif opcao == "2":
                for nome, endereco in AdministradorSistema.banco_centros_distribuicao.items():
                    print(f"Centro: {nome} | Endereço: {endereco}")

            elif opcao == "3":
                print("Voltando ao menu principal...")
                break
            else:
                print("Opção inválida.")
