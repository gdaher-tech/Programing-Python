import random

print('=====ROLETA DE NOMES=====')
nome = []

while True: ## Coletar nomes até o usuário digitar vazio
    nomes = input('Digite um nome ou aperte 1 para sair: ')
    if nomes == '1':
        break
    nome.append(nomes)

if not nomes:
    print("Nenhum nome foi inserido");

else:
    soteado = random.choice(nome)
    print('O nome soretado foi {}'.format(soteado))