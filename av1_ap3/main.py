from datetime import date

from classes_doador import Doador
from classes_receptores import Receptor
from classes_doacao import Doacao
from classes_CentroDistribuicao import CentroDistribuicao
from classes_intecao_doar import IntencaoDoar
from classes_administradores_sistema import AdministradorSistema

def testar_doador_e_intencao():
    print("\n=== Testando Doador e Intenção de Doar ===")
    
    # Criando doador
    doador = Doador(
        nome="Ana",
        idade=28,
        genero="Feminino",
        data_nascimento=date(1996, 5, 12),
        cidade_natal="São Paulo",
        estado_natal="SP",
        cpf="12345678900",  # Corrigido para 11 dígitos sem formatação
        profissao="Médica",
        cidade_residencia="São Paulo",
        estado_residencia="SP",
        estado_civil="solteiro",  # Corrigido para minúsculo
        tipo_sanguineo="O+",
        contato_emergencia="99999-9999"
    )
    doador.cadastrar()

    # Criando intenção de doar
    intencao = IntencaoDoar(data_intencao=date(2025, 6, 1))
    intencao.registrar_intencao_doar(doador)

    # Atualizando intenção
    intencao.atualizar_intencao_doar(novo_status="Confirmada")

    print("Doador cadastrado e intenção registrada!")

def testar_receptor_e_doacao():
    print("\n=== Testando Receptor e Doação ===")

    # Criando receptor
    receptor = Receptor(
        nome="Bruno",
        idade=35,
        genero="Masculino",
        data_nascimento=date(1989, 2, 10),
        cidade_natal="Rio de Janeiro",
        estado_natal="RJ",
        cpf="98765432100",  # Corrigido para só números
        profissao="Professor",
        cidade_residencia="Rio de Janeiro",
        estado_residencia="RJ",
        estado_civil="casado",  # Corrigido para minúsculo
        orgao_necessario="Rim",
        gravidade_condicao="Alta",
        centro_transplante_vinculado="Hospital das Clínicas",
        contato_emergencia="98888-7777",
        posicao_lista_espera="5"
    )
    receptor.cadastrar_receptor()

    # Criando doação
    doacao = Doacao(data_doacao=date(2025, 7, 1))
    doacao.registrar_intencao_doar()

    # Associação manual
    receptor.associar_doacao(doacao)
    doacao.associar_receptor(receptor)

    print("Receptor cadastrado e doação associada!")

def testar_centro_distribuicao():
    print("\n=== Testando Centro de Distribuição ===")

    centro = CentroDistribuicao(
        id=1,
        cidade="Brasília",
        estado="DF",
        endereco="Avenida Central, 1000",
        telefone="6133332222"
    )

    # Simulando adicionar itens ao estoque
    centro.estoque["Bolsas de Sangue"] = 10
    centro.estoque["Corações"] = 2
    centro.estoque["Fígados"] = 3

    print("\nEstoque atual do centro:")
    for produto, quantidade in centro.estoque.items():
        print(f"{produto}: {quantidade} unidades")

def testar_administrador():
    print("\n=== Testando Administrador Sistema ===")

    # Criando administrador
    admin = AdministradorSistema(
        nome="Admin",
        idade=40,
        genero="Masculino",
        data_nascimento=date(1984, 1, 1),
        cidade_natal="São Paulo",
        estado_natal="SP",
        cpf="11111111111",
        profissao="Administrador",
        cidade_residencia="São Paulo",
        estado_residencia="SP",
        estado_civil="casado",
        nome_usuario="admin",
        senha="admin123"
    )
    AdministradorSistema.banco_administradores[admin.nome_usuario] = admin

    # Simulando login
    try:
        admin.login(nome_usuario="admin", senha="admin123")
        print("Administrador logado com sucesso.")
        admin.logout()
    except ValueError as e:
        print(f"Erro no login: {e}")

if __name__ == "__main__":
    testar_doador_e_intencao()
    testar_receptor_e_doacao()
    testar_centro_distribuicao()
    testar_administrador()
