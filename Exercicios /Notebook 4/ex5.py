lista_de_orgaos = ["Coração", "Rins", "Fígado", "Pâncreas", "Pulmões"]

while True:
    print('''\nMenu de Opções
1 - Ver lista
2 - Adicionar Órgão
3 - Remover Órgão
4 - Adicionar múltiplos órgãos (sem duplicar)
5 - Sair''')

    opcao = int(input("Digite a opção desejada: \n"))

    # Opção 1 - Ver lista
    if opcao == 1:
        print("Lista Atual:", lista_de_orgaos)
        continuar = input("Deseja continuar? [s/n] ").lower()
        if continuar != "s":
            break

    # Opção 2 - Adicionar órgão
    elif opcao == 2:
        entrada = input("Digite o órgão que deseja adicionar à lista: ").strip()
        if entrada in lista_de_orgaos:
            print("Órgão já está na lista.")
        else:
            lista_de_orgaos.append(entrada)
            print(f"Órgão '{entrada}' adicionado com sucesso.")
            print("Lista Atual:", lista_de_orgaos)
        continuar = input("Deseja continuar? [s/n] ").lower()
        if continuar != "s":
            break

    # Opção 3 - Remover órgão
    elif opcao == 3:
        entrada = input("Digite o órgão que deseja remover da lista: ").strip()
        if entrada not in lista_de_orgaos:
            print("Órgão não encontrado na lista.")
        else:
            lista_de_orgaos.remove(entrada)
            print(f"Órgão '{entrada}' removido com sucesso.")
            print("Lista Atual:", lista_de_orgaos)
        continuar = input("Deseja continuar? [s/n] ").lower()
        if continuar != "s":
            break

    # Opção 4 - Adicionar múltiplos órgãos
    elif opcao == 4:
        entrada = input("Digite os órgãos separados por vírgula: ")
        novos_orgaos = entrada.split(",")

        for orgao in novos_orgaos:
            orgao = orgao.strip()
            if orgao in lista_de_orgaos:
                print(f"Órgão '{orgao}' já está na lista.")
            else:
                lista_de_orgaos.append(orgao)
                print(f"Órgão '{orgao}' foi adicionado à lista.")

        print("Lista Atual:", lista_de_orgaos)
        continuar = input("Deseja continuar? [s/n] ").lower()
        if continuar != "s":
            break

    # Opção 5 - Sair
    elif opcao == 5:
        print("Programa encerrado. Até mais!")
        break

    else:
        print("Opção inválida. Tente novamente.")
