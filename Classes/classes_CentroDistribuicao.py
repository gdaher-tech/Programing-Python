from typing import Dict
from uuid import uuid4

# Estados e cidades válidas
ESTADOS_VALIDOS = {'AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA',
    'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN',
    'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO'}  

CIDADES_PRINCIPAIS = {
    "AC": ["Rio Branco"],
    "AL": ["Maceió", "Arapiraca"],
    "AP": ["Macapá"],
    "AM": ["Manaus", "Parintins"],
    "BA": ["Salvador", "Feira de Santana", "Vitória da Conquista"],
    "CE": ["Fortaleza", "Caucaia", "Juazeiro do Norte"],
    "DF": ["Brasília", "Ceilândia", "Taguatinga", "Gama", "Samambaia"],
    "ES": ["Vitória", "Vila Velha", "Serra", "Cariacica"],
    "GO": ["Goiânia", "Aparecida de Goiânia", "Anápolis"],
    "MA": ["São Luís", "Imperatriz"],
    "MT": ["Cuiabá", "Várzea Grande", "Rondonópolis"],
    "MS": ["Campo Grande", "Dourados", "Três Lagoas"],
    "MG": ["Belo Horizonte", "Uberlândia", "Contagem", "Juiz de Fora", "Betim"],
    "PA": ["Belém", "Ananindeua", "Santarém"],
    "PB": ["João Pessoa", "Campina Grande", "Santa Rita"],
    "PR": ["Curitiba", "Londrina", "Maringá", "Ponta Grossa"],
    "PE": ["Recife", "Jaboatão dos Guararapes", "Olinda", "Caruaru"],
    "PI": ["Teresina", "Parnaíba", "Picos"],
    "RJ": ["Rio de Janeiro", "Niterói", "Duque de Caxias", "São Gonçalo", "Nova Iguaçu"],
    "RN": ["Natal", "Mossoró", "Parnamirim"],
    "RS": ["Porto Alegre", "Caxias do Sul", "Pelotas", "Canoas", "Santa Maria"],
    "RO": ["Porto Velho", "Ji-Paraná", "Ariquemes"],
    "RR": ["Boa Vista"],
    "SC": ["Florianópolis", "Joinville", "Blumenau", "Chapecó"],
    "SP": ["São Paulo", "Campinas", "Santos", "Guarulhos", "São Bernardo do Campo"],
    "SE": ["Aracaju", "Nossa Senhora do Socorro", "Lagarto"],
    "TO": ["Palmas", "Araguaína", "Gurupi"]
}


class CentroDistribuicao:
    """
    Centro físico que faz a logística da distribuição dos órgãos.
    """

    banco_centros = {}

    def __init__(self, numero_identificador: int, cidade: str, estado: str, endereco: str, telefone: str):
        # Validações básicas
        if not all(isinstance(x, str) and x.strip() for x in [cidade, estado, endereco, telefone]):
            raise ValueError("Todos os campos devem ser strings não vazias.")
        
        if estado not in ESTADOS_VALIDOS:
            raise ValueError(f"Estado inválido: {estado}.")
        
        if cidade not in CIDADES_PRINCIPAIS.get(estado, []):
            raise ValueError(f"A cidade '{cidade}' não pertence ao estado '{estado}'.")

        # Atributos
        self.__id = str(uuid4())
        self.numero_identificador = numero_identificador
        self.estado = estado
        self.cidade = cidade
        self.endereco = endereco
        self.telefone = telefone
        self.estoque: Dict[str, int] = {}

    @property
    def id(self) -> str:
        return self.__id

    def to_dict(self) -> Dict[str, str]:
        return {
            "id": self.id,
            "cidade": self.cidade,
            "estado": self.estado,
            "endereco": self.endereco,
            "telefone": self.telefone
        }

    def listar_estoque(self):
        if not self.estoque:
            print("Estoque vazio.")
        else:
            print(f"\n📦 Estoque do Centro {self.cidade} - {self.estado}:")
            for item, quantidade in self.estoque.items():
                print(f"  - {item}: {quantidade} unidades")

    def __str__(self):
        return f"Centro {self.cidade} ({self.estado}) - Tel: {self.telefone}"
