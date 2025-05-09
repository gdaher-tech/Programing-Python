import os
import random
import time
from datetime import datetime

# ======================
# Dados e Constantes
# ======================

lista_potenciais_doadores = []
lista_de_doacoes = []

lista_de_orgaos = [
    'Coração', 'Rins', 'Fígado', 'Pâncreas', 'Pulmões', 'Intestino',
    'Córneas', 'Pele', 'Ossos', 'Válvulas Cardíacas', 'Cartilagem',
    'Medula Óssea', 'Tendões', 'Vasos Sanguíneo',
    'Sangue de Cordão Umbilical', 'Sangue Universal'
]

lista_de_tipos_de_orgaos = [
    'Órgão','Órgão','Órgão','Órgão','Órgão', 'Órgão',
    'Tecido', 'Tecido', 'Tecido', 'Tecido', 'Tecido', 'Tecido',
    'Tecido', 'Tecido', 'Sangue', 'Sangue'
]

centros_de_distribuicao = ['Fortaleza', 'Salvador', 'Rio de Janeiro', 'São Paulo', 'Brasília']

estados = [
    'AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS',
    'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 'RS', 'RO', 'RR',
    'SC', 'SP', 'SE', 'TO'
]

estados_civis = [
    'solteiro', 'casado', 'divorciado', 'viúvo', 'separado', 'união estável'
]

# ======================
# Funções de Validação
# ======================

def validar_nome(nome):
    nome = nome.strip()
    return nome.replace(' ', '').isalpha() and len(nome) >= 3

def validar_idade(idade):
    return idade.isdigit()

def validar_sexo(sexo):
    sexo = sexo.strip().lower()
    if sexo in ('m', 'masculino'):
        return 'M'
    elif sexo in ('f', 'feminino'):
        return 'F'
    return None

def validar_data_nascimento(data_nascimento):
    try:
        datetime.strptime(data_nascimento, '%d/%m/%Y')
        return True
    except ValueError:
        return False

def validar_local_de_nascimento(local):
    local = local.strip()
    return local.replace(' ', '').isalpha() and len(local) >= 3

def validar_cpf(cpf):
    cpf = cpf.replace('.', '').replace('-', '').replace(' ', '')
    if not cpf.isdigit() or len(cpf) != 11:
        return False
    if cpf == cpf[0] * 11:
        return False
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    dig1 = (soma * 10) % 11
    if dig1 == 10:
        dig1 = 0
    if dig1 != int(cpf[9]):
        return False
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    dig2 = (soma * 10) % 11
    if dig2 == 10:
        dig2 = 0
    if dig2 != int(cpf[10]):
        return False
    return True

def validar_profissao(profissao):
    profissao = profissao.strip()
    return profissao.replace(' ', '').isalpha() and len(profissao) >= 3

def validar_cidade(cidade):
    cidade = cidade.strip()
    return cidade.replace(' ', '').isalpha() and len(cidade) >= 3

def validar_estado(sigla):
    return sigla.strip().upper() in estados

def validar_estado_civil(estado_civil):
    estado_civil = estado_civil.strip().lower()
    return estado_civil in estados_civis

def validar_orgao(orgao):
    orgao = orgao.strip().title()
    return orgao in lista_de_orgaos

# ======================
# Interface Inicial
# ======================

print('▓▓▓▓▓ SNDOT ▓▓▓▓▓')
print('╠ SEJA BEM-VINDO AO SISTEMA NACIONAL DE DOAÇÕES DE ÓRGÃOS ╣')
print('''
╠ INSIRA O NÚMERO REFERENTE À OPÇÃO DESEJADA:

    1. Cadastrar Doador
    2. Adicionar Doações
    3. Processar Doação
    4. Exibir estoque dos Centros de Distribuição
    5. Exibir histórico de Doações
    6. Finalizar Aplicação
''')

opcao = input('Insira a opção desejada: ')

if opcao == '1':
    print("*" * 30)
    print("Cadastrar Potencial Doador")
    print("*" * 30)

    while True:
        nome = input('Nome: ')
        if validar_nome(nome): break
        print('❌ Nome inválido.')

    while True:
        idade_input = input('Idade: ')
        if validar_idade(idade_input):
            idade = int(idade_input)
            if 18 <= idade <= 60: break
            print('❌ Idade fora da faixa permitida.')
        else:
            print('❌ Digite apenas números.')

    while True:
        sexo_input = input('Sexo (M/F): ')
        sexo = validar_sexo(sexo_input)
        if sexo: break
        print('❌ Sexo inválido.')

    while True:
        data_nascimento = input('Data de nascimento (dd/mm/aaaa): ')
        if validar_data_nascimento(data_nascimento): break
        print('❌ Data inválida.')

    while True:
        local_nascimento = input('Local de nascimento: ')
        if validar_local_de_nascimento(local_nascimento): break
        print('❌ Local inválido.')

    while True:
        cpf = input('CPF (xxx.xxx.xxx-xx): ')
        if validar_cpf(cpf): break
        print('❌ CPF inválido.')

    while True:
        profissao = input('Profissão: ')
        if validar_profissao(profissao): break
        print('❌ Profissão inválida.')

    while True:
        cidade = input('Cidade: ')
        if validar_cidade(cidade): break
        print('❌ Cidade inválida.')

    while True:
        estado = input('Estado (sigla, ex: SP): ').upper()
        if validar_estado(estado): break
        print('❌ Estado inválido.')

    while True:
        estado_civil = input('Estado civil: ').lower()
        if validar_estado_civil(estado_civil): break
        print('❌ Estado civil inválido.')

    lista_potenciais_doadores.append([
        nome, idade, sexo, data_nascimento, local_nascimento,
        cpf, profissao, cidade, estado, estado_civil
    ])

    print(f'✅ {nome} ({cpf}) cadastrado com sucesso em {cidade}-{estado}!')

elif opcao == '2':
    print("*" * 30)
    print("Adicionar Doações")
    print("*" * 30)

    cpf = input('Informe o CPF do potencial doador: ')
    lista_cpfs = [doador[6] for doador in lista_potenciais_doadores]

    if cpf not in lista_cpfs:
        print(f'❌ CPF {cpf} não está cadastrado.')
        print('➡ Por favor, insira a opção 1 do menu principal do SNDO para cadastrar o doador.')
    else:
        print(f'✅ CPF {cpf} encontrado. Vamos prosseguir com a doação.')

        print('\nÓrgãos disponíveis para doação:')
        for i, (orgao, tipo) in enumerate(zip(lista_de_orgaos, lista_de_tipos_de_orgaos)):
            print(f"[{i}] {orgao} (tipo: {tipo})")

        orgao = input('Digite o órgão que será doado: ')

        if not validar_orgao(orgao):
            print(f"❌ O órgão '{orgao}' não está disponível para doação.")
        else:
            lista_de_doacoes.append([cpf, orgao])
            print(f"✅ Órgão '{orgao}' cadastrado com sucesso para o doador {cpf}.")

            centro = random.choice(centros_de_distribuicao)
            print(f"🚚 A doação será encaminhada para o centro de distribuição: {centro}")