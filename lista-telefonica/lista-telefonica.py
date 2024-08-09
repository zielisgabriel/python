'''ADICIONAR'''
def adicionar_contato(agenda, nome, telefone):
    if nome in agenda:
        print('Este nome já existe na sua lista')
    else:
        print(f'{nome} foi adicionado a lista')
        agenda[nome] = telefone
        print(f'{agenda[nome]} foi adicionado no contato {nome}')

'''EXCLUIR'''
def excluir_contato(agenda, nome):
    if nome in agenda:
        del agenda[nome]
    else:
        print(f'O nome {nome} não se encontar na sua lista')

'''BUSCAR'''
def buscar_contato(agenda, nome):
    if nome in agenda:
        print (f'\nNome: {nome}, Telefone: {agenda[nome]}')
    else:
        print(f'\nNão existe {nome} na sua lista')

'''LISTAR'''
def listar_contato(agenda, nome):
    if not agenda:
        print('\nNão existe ninguém na agenda\n')
    else:
        for nome, agenda[nome] in agenda.items():
            print(f'Nome: {nome}, Telefone: {agenda[nome]}')

'''MENU'''
def menu_contato():
    print('\n--MENU--')
    print('1. Adicionar Contato')
    print('2. Excluir contato')
    print('3. Buscar contato')
    print('4. Listar contato')
    print('5. Sair')

'''CÓDIGO PRINCIPAL'''
def agenda_telefonica():
    agenda = {}

    while True:
        menu_contato()
        resposta = input ('Digite a opção:\n')
        if resposta == '1':
            nome = input('Digite o nome:\n')
            telefone = input('Digite o telefone:\n')
            adicionar_contato(agenda, nome, telefone)
        if resposta == '2':
            nome = input('Digite o nome:\n')
            excluir_contato(agenda, nome)
        if resposta == '3':
            nome = input('Digite o nome:\n')
            buscar_contato(agenda, nome)
        if resposta == '4':
            listar_contato(agenda, nome)
        if resposta == '5':
            print('\nSaindo...\n')
            break
        else:
            print('Opção inválida, tente novamente...\n')

agenda_telefonica()