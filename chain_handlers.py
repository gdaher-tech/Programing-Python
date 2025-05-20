

class Handler:
    def __init__(self):
        self._proximo = None

    def definir_proximo(self, proximo_handler):
        self._proximo = proximo_handler
        return proximo_handler  # permite encadeamento

    def processar(self, doador, receptor):
        if self._proximo:
            return self._proximo.processar(doador, receptor)
        return True

class CompatibilidadeSanguineaHandler(Handler):
    compatibilidade = {
        "O-": ["O-", "O+", "A-", "A+", "B-", "B+", "AB-", "AB+"],
        "O+": ["O+", "A+", "B+", "AB+"],
        "A-": ["A-", "A+", "AB-", "AB+"],
        "A+": ["A+", "AB+"],
        "B-": ["B-", "B+", "AB-", "AB+"],
        "B+": ["B+", "AB+"],
        "AB-": ["AB-", "AB+"],
        "AB+": ["AB+"]
    }

    def processar(self, doador, receptor):
        if receptor._tipo_sanguineo in self.compatibilidade.get(doador._tipo_sanguineo, []):
            print("Compatibilidade sanguínea verificada: Compatível.")
            return super().processar(doador, receptor)
        print("Compatibilidade sanguínea verificada: Incompatível.")
        print("Doação não realizada: Critérios não atendidos.")
        return False


class OrgaoNecessarioHandler(Handler):
    def processar(self, doador, receptor):
        if hasattr(doador, "orgaos_disponiveis") and receptor.orgao_necessario.lower() in [o.lower() for o in doador.orgaos_disponiveis]:
            print("Órgão necessário verificado: Compatível.")
            return super().processar(doador, receptor)
        print("Órgão necessário verificado: Incompatível.")
        print("Doação não realizada: Critérios não atendidos.")
        return False


class IntencaoDoacaoHandler(Handler):
    def processar(self, doador, receptor):
        if doador.intencao_doar and doador.intencao_doar.status.lower() in ["ativa", "s"]:
            print("Intenção de doação verificada: Positiva.")
            return super().processar(doador, receptor)
        print("Intenção de doação verificada: Negativa.")
        print("Doação não realizada: Critérios não atendidos.")
        return False


class GravidadeHandler(Handler):
    prioridade = {"Crítica": 3, "Grave": 2, "Moderada": 1, "Leve": 0}

    def processar(self, doador, receptor):
        gravidade = receptor.gravidade_condicao
        print(f"Gravidade da condição verificada: {gravidade} prioridade.")
        return super().processar(doador, receptor)
