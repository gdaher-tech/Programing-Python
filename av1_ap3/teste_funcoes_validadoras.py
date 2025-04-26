from datetime import date, timedelta
from validadores import (
    validar_nome,
    validar_idade,
    validar_genero,
    validar_dataNascimento,
    validar_cidadeNatal,
    validar_estadoNatal, 
    validar_cpf, 
    validar_profissao, 
    validar_cidadeResidencia, 
    validar_estadoResidencia, 
    validar_estadoCivil
)

def testar_validar_nome():
    print("Testando validar_nome()...")
    nomes_validos = ["Maria", "João Silva", "Ana"]
    nomes_invalidos = ["", "   ", "1234", "Ana1", 123, None]

    for nome in nomes_validos:
        try:
            validar_nome(nome)
            print(f"✅ '{nome}' válido")
        except Exception as e:
            print(f"❌ '{nome}' deveria ser válido, mas falhou: {e}")

    for nome in nomes_invalidos:
        try:
            validar_nome(nome)
            print(f"❌ '{nome}' inválido passou!")
        except Exception as e:
            print(f"✅ '{nome}' inválido corretamente detectado: {e}")

def testar_validar_idade():
    print("\nTestando validar_idade()...")
    idades_validas = [18, 25, 65]
    idades_invalidas = [-1, 0, 17, 66, "30", None]

    for idade in idades_validas:
        try:
            validar_idade(idade)
            print(f"✅ {idade} válida")
        except Exception as e:
            print(f"❌ {idade} deveria ser válida, mas falhou: {e}")

    for idade in idades_invalidas:
        try:
            validar_idade(idade)
            print(f"❌ {idade} inválida passou!")
        except Exception as e:
            print(f"✅ {idade} inválida corretamente detectada: {e}")

def testar_validar_genero():
    print("\nTestando validar_genero()...")
    generos_validos = ["F", "Masculino", "Outro"]
    generos_invalidos = ["", "   ", "123", 123, None]

    for genero in generos_validos:
        try:
            validar_genero(genero)
            print(f"✅ '{genero}' válido")
        except Exception as e:
            print(f"❌ '{genero}' deveria ser válido, mas falhou: {e}")

    for genero in generos_invalidos:
        try:
            validar_genero(genero)
            print(f"❌ '{genero}' inválido passou!")
        except Exception as e:
            print(f"✅ '{genero}' inválido corretamente detectado: {e}")

def testar_validar_dataNascimento():
    print("\nTestando validar_dataNascimento()...")
    try:
        validar_dataNascimento(date(2000, 1, 1))
        print("✅ Teste 1 (data válida) passou")
    except Exception as e:
        print("❌ Teste 1 falhou:", e)

    try:
        validar_dataNascimento(date.today() + timedelta(days=1))
        print("❌ Teste 2 (futuro) falhou (esperado erro)")
    except ValueError as e:
        print("✅ Teste 2 (data futura) passou:", e)

    try:
        validar_dataNascimento("2000-01-01")
        print("❌ Teste 3 (tipo inválido) falhou (esperado erro)")
    except TypeError as e:
        print("✅ Teste 3 (tipo inválido) passou:", e)

def testar_validar_cidadeNatal():
    print("\nTestando validar_cidadeNatal()...")
    try:
        validar_cidadeNatal("São Paulo")
        print("✅ Teste 1 (válida) passou")
    except Exception as e:
        print("❌ Teste 1 falhou:", e)

    try:
        validar_cidadeNatal("Rio123")
        print("❌ Teste 2 (inválida com número) falhou (esperado erro)")
    except ValueError as e:
        print("✅ Teste 2 passou:", e)

    try:
        validar_cidadeNatal(123)
        print("❌ Teste 3 (tipo inválido) falhou (esperado erro)")
    except TypeError as e:
        print("✅ Teste 3 passou:", e)

    try:
        validar_cidadeNatal("   ")
        print("❌ Teste 4 (só espaços) falhou (esperado erro)")
    except ValueError as e:
        print("✅ Teste 4 passou:", e)

def testar_validar_estadoNatal():
    print("\nTestando validar_estadoNatal()...")
    
    # Teste 1 – Estado válido
    try:
        validar_estadoNatal("Minas Gerais")
        print("✅ Teste 1 (válido) passou")
    except Exception as e:
        print("❌ Teste 1 falhou:", e)

    # Teste 2 – Estado com número
    try:
        validar_estadoNatal("Rio1")
        print("❌ Teste 2 (inválido com número) falhou (esperado erro)")
    except ValueError as e:
        print("✅ Teste 2 passou:", e)

    # Teste 3 – Tipo inválido
    try:
        validar_estadoNatal(123)
        print("❌ Teste 3 (tipo inválido) falhou (esperado erro)")
    except TypeError as e:
        print("✅ Teste 3 passou:", e)

    # Teste 4 – String só com espaços
    try:
        validar_estadoNatal("   ")
        print("❌ Teste 4 (só espaços) falhou (esperado erro)")
    except ValueError as e:
        print("✅ Teste 4 passou:", e)

def testar_validar_cpf():
    print("\nTestando validar_cpf()...")

    # Teste 1 – CPF válido (formato string, 11 dígitos)
    try:
        validar_cpf("12345678901")
        print("✅ Teste 1 passou (CPF válido)")
    except Exception as e:
        print("❌ Teste 1 falhou:", e)

    # Teste 2 – CPF com letras
    try:
        validar_cpf("1234abc8901")
        print("❌ Teste 2 falhou (esperado erro)")
    except ValueError as e:
        print("✅ Teste 2 passou:", e)

    # Teste 3 – CPF com menos dígitos
    try:
        validar_cpf("12345678")
        print("❌ Teste 3 falhou (esperado erro)")
    except ValueError as e:
        print("✅ Teste 3 passou:", e)

    # Teste 4 – Tipo inválido (int)
    try:
        validar_cpf(12345678901)
        print("❌ Teste 4 falhou (esperado erro)")
    except TypeError as e:
        print("✅ Teste 4 passou:", e)

    # Teste 5 – CPF com formatação (pontos e traço)
    try:
        validar_cpf("123.456.789-01")
        print("✅ Teste 5 passou (formatação aceita)")
    except Exception as e:
        print("❌ Teste 5 falhou:", e)

testar_validar_cpf()

def testar_validar_profissao():
    print("\nTestando validar_profissao()...")

    # Teste 1 – Profissão válida
    try:
        validar_profissao("Engenheiro Civil")
        print("✅ Teste 1 passou (profissão válida)")
    except Exception as e:
        print("❌ Teste 1 falhou:", e)

    # Teste 2 – Profissão com números
    try:
        validar_profissao("Médico123")
        print("❌ Teste 2 falhou (esperado erro)")
    except ValueError as e:
        print("✅ Teste 2 passou:", e)

    # Teste 3 – Tipo inválido (int)
    try:
        validar_profissao(123)
        print("❌ Teste 3 falhou (esperado erro)")
    except TypeError as e:
        print("✅ Teste 3 passou:", e)

    # Teste 4 – Profissão vazia
    try:
        validar_profissao("   ")
        print("❌ Teste 4 falhou (esperado erro)")
    except ValueError as e:
        print("✅ Teste 4 passou:", e)

def testar_validar_cidadeResidencia():
    print("\nTestando validar_cidadeResidencia()...")

    try:
        validar_cidadeResidencia("São Paulo")
        print("✅ Teste 1 passou")
    except Exception as e:
        print("❌ Teste 1 falhou:", e)

    try:
        validar_cidadeResidencia("123Rio")
        print("❌ Teste 2 falhou (esperado erro)")
    except ValueError as e:
        print("✅ Teste 2 passou:", e)

    try:
        validar_cidadeResidencia(123)
        print("❌ Teste 3 falhou (esperado erro)")
    except TypeError as e:
        print("✅ Teste 3 passou:", e)

    try:
        validar_cidadeResidencia("   ")
        print("❌ Teste 4 falhou (esperado erro)")
    except ValueError as e:
        print("✅ Teste 4 passou:", e)

def testar_validar_estadoResidencia():
    print("\nTestando validar_estadoResidencia()...")

    try:
        validar_estadoResidencia("Minas Gerais")
        print("✅ Teste 1 passou")
    except Exception as e:
        print("❌ Teste 1 falhou:", e)

    try:
        validar_estadoResidencia("Bahia123")
        print("❌ Teste 2 falhou (esperado erro)")
    except ValueError as e:
        print("✅ Teste 2 passou:", e)

    try:
        validar_estadoResidencia(987)
        print("❌ Teste 3 falhou (esperado erro)")
    except TypeError as e:
        print("✅ Teste 3 passou:", e)

    try:
        validar_estadoResidencia(" ")
        print("❌ Teste 4 falhou (esperado erro)")
    except ValueError as e:
        print("✅ Teste 4 passou:", e)

def testar_validar_estadoCivil():
    print("\nTestando validar_estadoCivil()...")

    try:
        validar_estadoCivil("Casado")
        print("✅ Teste 1 passou")
    except Exception as e:
        print("❌ Teste 1 falhou:", e)

    try:
        validar_estadoCivil("Divorciado")
        print("❌ Teste 2 falhou (esperado erro)")
    except ValueError as e:
        print("✅ Teste 2 passou:", e)

    try:
        validar_estadoCivil(123)
        print("❌ Teste 3 falhou (esperado erro)")
    except TypeError as e:
        print("✅ Teste 3 passou:", e)

    try:
        validar_estadoCivil("   ")
        print("❌ Teste 4 falhou (esperado erro)")
    except ValueError as e:
        print("✅ Teste 4 passou:", e)


# Executar todos os testes
if __name__ == "__main__":
    testar_validar_nome()
    testar_validar_idade()
    testar_validar_genero()
    testar_validar_dataNascimento()
    testar_validar_cidadeNatal()
    testar_validar_estadoNatal()
    testar_validar_cpf()
    testar_validar_profissao()
    testar_validar_cidadeResidencia()
    testar_validar_estadoResidencia()
    testar_validar_estadoCivil()


