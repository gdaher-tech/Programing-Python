from datetime import date
from Classes import Doador, Receptor, IntencaoDoar, Doacao

def criar_doador():
    doador = Doador(
        nome="Lucas Silva",
        idade=30,
        genero="Masculino",
        data_nascimento=date(1994, 5, 15),
        cidade_natal="São Paulo",
        estado_natal="SP",
        cpf="11122233344",
        profissao="Engenheiro",
        cidade_residencia="São Paulo",
        estado_residencia="SP",
        estado_civil="solteiro",
        tipo_sanguineo="O+",
        contato_emergencia="11999999999",
        orgaos_disponiveis=["coracao", "rim"]
    )
    doador.cadastrar()

    intencao = IntencaoDoar(date.today(), status="Ativa")
    intencao.registrar_intencao_doar(doador)

    return doador

def criar_receptor():
    receptor = Receptor(
        nome="Maria Oliveira",
        idade=45,
        genero="Feminino",
        data_nascimento=date(1979, 8, 10),
        cidade_natal="Rio de Janeiro",
        estado_natal="RJ",
        cpf="55566677788",
        profissao="Professora",
        cidade_residencia="Rio de Janeiro",
        estado_residencia="RJ",
        estado_civil="casado",
        orgao_necessario="coracao",
        gravidade_condicao="Grave",
        centro_transplante_vinculado="Hospital do Coração RJ",
        contato_emergencia="21988887777",
        posicao_lista_espera="3"
    )
    receptor.cadastrar()
    return receptor

if __name__ == "__main__":
    doador = criar_doador()
    receptor = criar_receptor()

    print("\n✅ Doador e receptor criados com sucesso!")
    print("Doador:", doador.listar())
    print("Receptor:", receptor.listar())
