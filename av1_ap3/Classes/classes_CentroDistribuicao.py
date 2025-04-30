from typing import Dict
from uuid import uuid4

# Listas dos estados Válidos para a classe se basear 

ESTADOS_VALIDOS = {'AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO'}

# Dicionário das principais cidades destes Estados

CIDADES_PRINCIPAIS = {

    "AC": ["Rio Branco"],
    "AL": ["Maceió"],
    "AP": ["Macapá"],
    "AM": ["Manaus"],
    "BA": ["Salvador", "Feira de Santana"],
    "CE": ["Fortaleza", "Juazeiro do Norte"],
    "DF": ["Brasília", "Ceilândia", "Taguatinga"],
    "ES": ["Vitória", "Vila Velha"],
    "GO": ["Goiânia", "Aparecida de Goiânia"],
    "MA": ["São Luís", "Imperatriz"],
    "MT": ["Cuiabá", "Várzea Grande"],
    "MS": ["Campo Grande", "Dourados"],
    "MG": ["Belo Horizonte", "Uberlândia", "Contagem"],
    "PA": ["Belém", "Ananindeua"],
    "PB": ["João Pessoa", "Campina Grande"],
    "PR": ["Curitiba", "Londrina", "Maringá"],
    "PE": ["Recife", "Jaboatão dos Guararapes"],
    "PI": ["Teresina", "Parnaíba"],
    "RJ": ["Rio de Janeiro", "Niterói", "Duque de Caxias"],
    "RN": ["Natal", "Mossoró"],
    "RS": ["Porto Alegre", "Caxias do Sul"],
    "RO": ["Porto Velho", "Ji-Paraná"],
    "RR": ["Boa Vista"],
    "SC": ["Florianópolis", "Joinville", "Blumenau"],
    "SP": ["São Paulo", "Campinas", "Santos"],
    "SE": ["Aracaju", "Nossa Senhora do Socorro"],
    "TO": ["Palmas", "Araguaína"]

}

class CentroDistribuicao: 

    banco_centros = {}

    """
    Centro físico que faz a logística da distribuição dos órgãos. 

    __id (int): Define uma chave única para o Centro de Distribuição. 
    cidade (str): Cidade em que está localizado o Centro de Distribuição.
    estado (str): Estado em que etá localizado o Centro de Distribuição.
    endereco (str) : Endereço do Centro de Distribuição.

    """

    def __init__(self, id : int, cidade : str, estado : str, endereco : str, telefone):



        """
        Construtor da Classe CentroDistribuicao

        Parâmetros: 
            id (int): Identificador único do Centro de Distribuição. 
            cidade (str): Representa a cidade a qual o Centro de Distribuição esta localizado. 
            estado (str): Representa o estado a qual o Centro de Distribuição esta localizado.
            endereco(str): Representa o endereço do Centro de Distribuição. 
            telefone(str): Representa o Telefone do Centro de Distribuição. 
        """

        # Validação ID 
        if not all(isinstance(x, str) and x.strip() for x in [cidade, estado, endereco, telefone]):
            raise ValueError("Todos os campos devem ser strings não vazias.")
        
        # Atributo Protegido
        self.__id : str = str(uuid4())      # Gerando id aletório e único para CT.

        # Atributos Públicos 
        self.estado: str = estado       # Atributo estado do tipo str 
        self.cidade: str = cidade       # Atributo cidade do tipo str
        self.endereco: str = endereco   # Atributo endereço do tipo str  
        self.telefone: str = telefone   # Atributo telefone do tipo str 
        self.estoque = {}

    @property 
    def id(self) -> int:

        """
        Retorna o identificador do Centro de Distribuição  
        Este atributo é somente leitura 
        """

        return self.__id
    
  

    def to_dict(self) -> Dict[str, str]:
        return {
        "id": str(self.id),
        "cidade": self.cidade,
        "estado": self.estado,
        "endereco": self.endereco,
        "telefone": self.telefone
    }


    


        

        