from datetime import date, datetime
from Classes import Doador, Receptor, AdministradorSistema, IntencaoDoar, Doacao, CentroDistribuicao
from Utils.importacaoes import importar_doadores, importar_receptores, importar_administradores
from chain_handlers import (
    CompatibilidadeSanguineaHandler,
    OrgaoNecessarioHandler,
    IntencaoDoacaoHandler,
    GravidadeHandler
)
from testeChain import criar_doador, criar_receptor

def mostrar_dados_importados():
    print("\n=== Doadores Importados ===")
    for doador in Doador.banco_doador.values():
        print(doador.listar())

    print("\n=== Receptores Importados ===")
    for receptor in Receptor.banco_receptores.values():
        print(receptor.listar())

    print("\n=== Administradores Importados ===")
    for admin in AdministradorSistema.banco_administradores.values():
        print(admin.listar())

def cadastrar_doador_manual():
    try:
        print("\n--- Cadastro de Novo Doador ---")
        nome = input("Nome: ")
        idade = int(input("Idade: "))
        genero = input("Gênero: ")
        data_nascimento = datetime.strptime(input("Data de nascimento (AAAA-MM-DD): "), "%Y-%m-%d").date()
        cidade_natal = input("Cidade natal: ")
        estado_natal = input("Estado natal: ")
        cpf = input("CPF: ")
        profissao = input("Profissão: ")
        cidade_residencia = input("Cidade de residência: ")
        estado_residencia = input("Estado de residência: ")
        estado_civil = input("Estado civil: ")
        tipo_sanguineo = input("Tipo sanguíneo: ")
        contato_emergencia = input("Contato de emergência: ")
        orgaos = input("Órgãos disponíveis para doação (separados por vírgula): ").split(",")

        doador = Doador(nome, idade, genero, data_nascimento, cidade_natal, estado_natal,
                        cpf, profissao, cidade_residencia, estado_residencia, estado_civil,
                        tipo_sanguineo, contato_emergencia, [o.strip().lower() for o in orgaos])
        doador.cadastrar()
    except Exception as e:
        print(f"Erro ao cadastrar doador: {e}")

def registrar_intencao():
    cpf = input("CPF do doador: ")
    doador = Doador.banco_doador.get(cpf)
    if doador:
        intencao = IntencaoDoar(date.today())
        intencao.registrar_intencao_doar(doador)
    else:
        print("Doador não encontrado.")

def cadastrar_receptor_manual():
    try:
        print("\n--- Cadastro de Novo Receptor ---")
        nome = input("Nome: ")
        idade = int(input("Idade: "))
        genero = input("Gênero: ")
        data_nascimento = datetime.strptime(input("Data de nascimento (AAAA-MM-DD): "), "%Y-%m-%d").date()
        cidade_natal = input("Cidade natal: ")
        estado_natal = input("Estado natal: ")
        cpf = input("CPF: ")
        profissao = input("Profissão: ")
        cidade_residencia = input("Cidade de residência: ")
        estado_residencia = input("Estado de residência: ")
        estado_civil = input("Estado civil: ")
        orgao_necessario = input("Órgão necessário: ")
        gravidade = input("Gravidade da condição (Leve, Moderada, Grave, Crítica): ")
        centro = input("Centro de transplante vinculado: ")
        contato_emergencia = input("Contato de emergência: ")
        posicao = input("Posição na lista de espera: ")

        receptor = Receptor(nome, idade, genero, data_nascimento, cidade_natal, estado_natal,
                            cpf, profissao, cidade_residencia, estado_residencia, estado_civil,
                            orgao_necessario, gravidade, centro, contato_emergencia, posicao)
        receptor.tipo_sanguineo = input("Tipo sanguíneo do receptor: ")
        receptor.cadastrar()
    except Exception as e:
        print(f"Erro ao cadastrar receptor: {e}")

def cadastrar_centro_distribuicao():
    try:
        numero = int(input("Número identificador: "))
        cidade = input("Cidade: ")
        estado = input("Estado: ")
        endereco = input("Endereço: ")
        telefone = input("Telefone: ")
        centro = CentroDistribuicao(numero, cidade, estado, endereco, telefone)
        CentroDistribuicao.banco_centros[centro.id] = centro
        print("Centro de distribuição cadastrado com sucesso.")
    except Exception as e:
        print(f"Erro ao cadastrar centro: {e}")

def avaliar_doacao():
    cpf_doador = input("CPF do doador: ")
    cpf_receptor = input("CPF do receptor: ")

    doador = Doador.banco_doador.get(cpf_doador)
    receptor = Receptor.banco_receptores.get(cpf_receptor)

    if not doador or not receptor:
        print("Doador ou receptor não encontrados.")
        return

    if not hasattr(receptor, '_tipo_sanguineo'):
        receptor._tipo_sanguineo = getattr(receptor, 'tipo_sanguineo', None)

    h1 = CompatibilidadeSanguineaHandler()
    h2 = OrgaoNecessarioHandler()
    h3 = IntencaoDoacaoHandler()
    h4 = GravidadeHandler()

    h1.definir_proximo(h2).definir_proximo(h3).definir_proximo(h4)

    print("\n--- Avaliação de Doação ---")
    if h1.processar(doador, receptor):
        print("✅ Doação pode ser realizada!")
    else:
        print("❌ Doação não realizada.")

def main():
    print("Importando dados do sistema...\n")
    try:
        importar_doadores('Utils/doadores.json')
        importar_receptores('Utils/receptores.json')
        importar_administradores('Utils/administradores.json')
    except FileNotFoundError as e:
        print(f"Erro: arquivo não encontrado - {e.filename}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

    # Criar doador e receptor de teste
    doador_teste = criar_doador()
    receptor_teste = criar_receptor()
    receptor_teste._tipo_sanguineo = receptor_teste.__dict__.get('_tipo_sanguineo', 'A+')
    print("\n✅ Doador e receptor de teste foram criados.")
    print(f"🔹 CPF do Doador de teste: {doador_teste.cpf}")
    print(f"🔹 CPF do Receptor de teste: {receptor_teste.cpf}")

    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("1. Mostrar dados importados")
        print("2. Cadastrar novo doador")
        print("3. Registrar intenção de doação")
        print("4. Cadastrar novo receptor")
        print("5. Cadastrar centro de distribuição")
        print("6. Avaliar possibilidade de doação")
        print("7. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            mostrar_dados_importados()
        elif opcao == "2":
            cadastrar_doador_manual()
        elif opcao == "3":
            registrar_intencao()
        elif opcao == "4":
            cadastrar_receptor_manual()
        elif opcao == "5":
            cadastrar_centro_distribuicao()
        elif opcao == "6":
            avaliar_doacao()
        elif opcao == "7":
            print("Saindo do sistema.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
