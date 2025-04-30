import json
from datetime import datetime
from Classes.classes_doador import Doador
from Classes.classes_receptores import Receptor
from Classes.classes_administradores_sistema import AdministradorSistema

def importar_doadores(caminho_arquivo):
    print(">>> Importando doadores...")
    with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
        dados = json.load(arquivo)

    for item in dados:  #Implementar validacao do arquivo json 
        pessoa = item["dados"]
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
        print(
            f"[DOADOR] {pessoa['nome']} | CPF: {pessoa['cpf']} | Idade: {pessoa['idade']} | "
            f"Tipo Sanguíneo: {pessoa['tipo_sanguineo']} | Cidade: {pessoa['cidade_residencia']}/{pessoa['estado_residencia']} | "
            f"Status de Intenção: {item['intencao']['status']}"
        )

def importar_receptores(caminho_arquivo):
    print(">>> Importando receptores...")
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
        print(
            f"[RECEPTOR] {pessoa['nome']} | CPF: {pessoa['cpf']} | Órgão Necessário: {necessidade['orgao_necessario']} | "
            f"Gravidade: {necessidade['gravidade_condicao']} | Lista de Espera: {necessidade['posicao_lista_espera']}"
        )

def importar_administradores(caminho_arquivo):
    print(">>> Importando administradores...")
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
        print(
            f"[ADMIN] {pessoa['nome']} | CPF: {pessoa['cpf']} | Usuário: {acesso['nome_usuario']}"
        )
