from abc import ABC, abstractmethod
from datetime import date
from uuid import uuid4

class Pessoa(ABC):
    """
    Classe abstrata que representa uma pessoa no sistema SNDOT.

    Essa classe serve como base para outras classes (como Doador, Receptor e AdministradorSistema),
    e define os atributos e métodos comuns a todas as pessoas envolvidas.

    Atributos:
        __id (str): Identificador único (UUID).
        _nome (str): Nome da pessoa.
        _idade (int): Idade da pessoa.
        _genero (str): Gênero da pessoa.
        _data_nascimento (date): Data de nascimento.
        _cidade_natal (str): Cidade natal.
        _estado_natal (str): Estado natal.
        __cpf (str): CPF (privado).
        __profissao (str): Profissão.
        __cidade_residencia (str): Cidade onde reside.
        __estado_residencia (str): Estado onde reside.
        _estado_civil (str): Estado civil.
    """

    def __init__(self, nome: str, idade: int, genero: str, data_nascimento: date,
                 cidade_natal: str, estado_natal: str, cpf: str, profissao: str,
                 cidade_residencia: str, estado_residencia: str, estado_civil: str):
        
        self.__id = str(uuid4())
        self._nome = nome
        self._idade = idade
        self._genero = genero
        self._data_nascimento = data_nascimento
        self._cidade_natal = cidade_natal
        self._estado_natal = estado_natal
        self.__cpf = cpf
        self.__profissao = profissao
        self.__cidade_residencia = cidade_residencia
        self.__estado_residencia = estado_residencia
        self._estado_civil = estado_civil

    @abstractmethod
    def cadastrar(self): pass

    @abstractmethod
    def editar(self): pass

    @abstractmethod
    def listar(self): pass

    @abstractmethod
    def buscar(self): pass

    @abstractmethod
    def excluir(self): pass
