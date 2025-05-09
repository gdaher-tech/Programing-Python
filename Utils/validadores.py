from Classes import pessoa
from datetime import date 

import re

def validar_nome(nome: str):
    if not isinstance(nome, str):
        raise TypeError("Nome deve ser do tipo str")

    nome_limpo = nome.strip()
    if not nome_limpo:
        raise ValueError("Nome não pode ser vazio")

    # ✅ Permite letras, espaços, pontos, hífens e acentos
    if not re.match(r"^[A-Za-zÀ-ÖØ-öø-ÿ\s\.\-]+$", nome_limpo):
        raise ValueError("Nome deve conter apenas letras, espaços, pontos e hífens")

        

def validar_idade(idade: int):
    if not isinstance(idade, int):
        raise TypeError("A idade deve ser do tipo int")

    if idade < 0 or idade > 130:
        raise ValueError("A idade deve estar entre 0 e 130 anos")

      

# Validação de gênero
def validar_genero(genero: str):
    # VALIDAÇÃO DE TIPO 
    if not isinstance(genero, str):
        raise TypeError("Gênero deve ser uma string.")
    
    # VALIDAÇÃO DE VALOR
    if not genero.strip():
        raise ValueError("Gênero não pode estar vazio.")
    
    if not genero.replace(" ", "").isalpha():
        raise ValueError("Gênero deve conter apenas letras.")

# Validação de Data de Nascimento
def validar_dataNascimento(data_nascimento : date): 
    # VALIDAÇÃO DE TIPO 
    if not isinstance(data_nascimento, date):
        raise TypeError("A data de nascimento deve ser do tipo Date")
    
    # VALIDAÇÃO DE VALOR 
    hoje = date.today()     # Define a data em que o programa foi aberto 

    if data_nascimento > hoje:
        raise ValueError("O ano de nascimento não pode ser maior que o ano em que estamos")
    
def validar_cidadeNatal(cidade_natal : str): 
    # VALIDAÇÃO DE TIPO 
    if not isinstance(cidade_natal, str): 
        raise TypeError("Cidade Natal deve ser do tipo String")
    
    # VALIDAÇÃO DE VALOR 
    cidade_limpa = cidade_natal.strip()

    if not cidade_limpa or not cidade_limpa.replace(" ", "").isalpha(): 
        raise ValueError("Cidade Natal deve conter apenas Letras")
    
def validar_estadoNatal(estado_natal : str):
    # VALIDAÇÃO DE TIPO 
    if not isinstance(estado_natal, str): 
        raise TypeError("Estado Natal deve conter apenas letras")
    
    # VALIDAÇÃO DE VALOR
    estado_limpo = estado_natal.strip()

    if not estado_limpo or not estado_limpo.replace(" ","").isalpha(): 
        raise ValueError("Estado Natal deve conter apenas letras e não pod estar vazio")
    
def validar_cpf(cpf : str): 
    # VALIDAÇÃO DE TIPO
    if not isinstance(cpf, str): 
        raise TypeError("CPF deve ser String")
        
    # VALIDAÇÃO DE VALOR
    if not cpf.isdigit(): 
        raise ValueError("O CPF deve conter apenas números")

    if len(cpf) != 11: 
        raise ValueError("O CPF deve conter 11 dígitos")

    
def validar_profissao(profissao : str): 
    # VALIDAÇÃO DE TIPO
    if not isinstance(profissao, str): 
        raise TypeError("CPF deve ser String")
    
    # VALIDAÇÃO DE VALOR

    profissao_limpa = profissao.strip()

    if not profissao_limpa or not profissao_limpa.replace(" ", "").isalpha(): 
        raise ValueError("Profissão deve conter apenas letras e não pode estar vazia")
    
def validar_cidadeResidencia(cidade_residencia : str): 
    # VALIDAÇÃO DE TIPO 
    if not isinstance(cidade_residencia, str): 
        raise TypeError("Cidade Natal deve ser do tipo String")
    
    # VALIDAÇÃO DE VALOR 
    cidade_limpa = cidade_residencia.strip()

    if not cidade_limpa or not cidade_limpa.replace(" ", "").isalpha(): 
        raise ValueError("Cidade Natal deve conter apenas Letras")
    
def validar_estadoResidencia(estado_residencia : str): 
    # VALIDAÇÃO DE TIPO 
    if not isinstance(estado_residencia, str): 
        raise TypeError("Estado Natal deve conter apenas letras")
    
    # VALIDAÇÃO DE VALOR
    estado_limpo = estado_residencia.strip()

    if not estado_limpo or not estado_limpo.replace(" ","").isalpha(): 
        raise ValueError("Estado Natal deve conter apenas letras e não pod estar vazio")
    
def validar_estadoCivil(estado_civil: str):
    if not isinstance(estado_civil, str):
        raise TypeError("Estado Civil deve ser do tipo string")

    estado_limpo = estado_civil.strip().lower()

    # Lista corrigida de estados civis permitidos
    estados_civis = ['casado', 'solteiro', 'uniao estavel', 'viuvo', 'divorciado']

    if not estado_limpo or not estado_limpo.replace(" ", "").isalpha():
        raise ValueError("Estado Civil deve conter apenas letras e não pode estar vazio")

    if estado_limpo not in estados_civis:
        raise ValueError("Este estado civil não é válido")






    





    
    



    


    

    

