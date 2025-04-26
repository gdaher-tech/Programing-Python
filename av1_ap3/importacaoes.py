import json
from datetime import datetime
from classes_doador import Doador
from classes_receptores import Receptor
from classes_administradores_sistema import AdministradorSistema

def importar_doadores(caminho_arquivo):
    """
    Importa doadores de um arquivo JSON.
    """
    with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
        dados = json.load(arquivo)

    for item in dados:
        pessoa = item["dados"]

        # Corrigir formato de data para YYYY-MM-DD
        data_corrigida = datetime.strptime(pessoa["data_nascimento"], "%d/%m/%Y").date()

        novo_doador = Doador(
            nome=pessoa['nome'],
            idade=pessoa['idade'],
            genero=pessoa['sexo'],
            data_nascimento=data_corrigida,
            cidade_natal=pessoa['cidade_natal'],
            estado_natal=pessoa['estado_natal'],
            cpf=pessoa['cpf'],
            profissao=pessoa['profissao'],
            cidade_residencia=pessoa['cidade_residencia'],
            estado_residencia=pessoa['estado_residencia'],
            estado_civil=pessoa['estado_civil'].lower(),
            tipo_sanguineo=pessoa['tipo_sanguineo'],
            contato_emergencia=pessoa['contato_emergencia']
        )
        novo_doador.cadastrar()
    print("Doadores importados com sucesso.")


def importar_receptores(caminho_arquivo):
    """
    Importa receptores de um arquivo JSON.
    """
    with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
        dados = json.load(arquivo)

    for item in dados:
        pessoa = item["dados"]
        necessidade = item["necessidade"]

        data_corrigida = datetime.strptime(pessoa["data_nascimento"], "%d/%m/%Y").date()

        novo_receptor = Receptor(
            nome=pessoa['nome'],
            idade=pessoa['idade'],
            genero=pessoa['sexo'],
            data_nascimento=data_corrigida,
            cidade_natal=pessoa['cidade_natal'],
            estado_natal=pessoa['estado_natal'],
            cpf=pessoa['cpf'],
            profissao=pessoa['profissao'],
            cidade_residencia=pessoa['cidade_residencia'],
            estado_residencia=pessoa['estado_residencia'],
            estado_civil=pessoa['estado_civil'].lower(),
            orgao_necessario=necessidade['orgao_necessario'],
            gravidade_condicao=necessidade['gravidade_condicao'],
            centro_transplante_vinculado=necessidade['centro_transplante'],
            contato_emergencia=pessoa['contato_emergencia'],
            posicao_lista_espera=str(necessidade['posicao_lista_espera'])
        )
        novo_receptor.cadastrar_receptor()
    print("Receptores importados com sucesso.")


def importar_administradores(caminho_arquivo):
    """
    Importa administradores de um arquivo JSON.
    """
    with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
        dados = json.load(arquivo)

    for item in dados:
        pessoa = item["dados"]
        acesso = item["acesso"]

        data_corrigida = datetime.strptime(pessoa["data_nascimento"], "%d/%m/%Y").date()

        novo_admin = AdministradorSistema(
            nome=pessoa['nome'],
            idade=pessoa['idade'],
            genero=pessoa['sexo'],
            data_nascimento=data_corrigida,
            cidade_natal=pessoa['cidade_natal'],
            estado_natal=pessoa['estado_natal'],
            cpf=pessoa['cpf'],
            profissao=pessoa['profissao'],
            cidade_residencia=pessoa['cidade_residencia'],
            estado_residencia=pessoa['estado_residencia'],
            estado_civil=pessoa['estado_civil'].lower(),
            nome_usuario=acesso['nome_usuario'],
            senha=acesso['senha']
        )
        novo_admin.cadastrar()
    print("Administradores importados com sucesso.")
