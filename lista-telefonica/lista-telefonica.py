def adicionar_contato(agenda, nome, telefone):
    if nome in agenda:
        print(f'{nome} já está na sua agenda')
    else:
        print(f'Adicionando {nome} na lista')
        agenda[nome] = telefone
        print(f'{agenda[nome]} foi salvo no contato {nome}')

def excluir_contato(agenda, nome):
    if nome in agenda:
        del agenda[nome]
        print (f'{nome} foi removido da sua lista de contatos')
    else:
        print (f'Não existe nenhum contato chamado {nome}')

def listar_contato(agenda, nome, telefone):
    if not agenda:
        print('Não exite nenhum contato na sua lista')
    else:
        print('Lista telefônica\n')
        for nome, telefone in agenda.items():
            print(f'Nome: {nome}, Telefone: {telefone}')
        
def buscar_contato(agenda, nome):
    if nome in agenda:
        print(f'Nome: {nome}, Telefone: {agenda[nome]}')
    else:
        (f'{nome} não encontrado')

def exibir_menu():
    print('\nMenu')
    print('1. Adicionar Contato')
    print('2. Excluir Contato')
    print('3. Listar Contato')
    print('4. Buscar Contato')
    print('5. Sair')

'''CÓDIGO PRINCIPAL'''
def agenda_telefonica():
    agenda = {}

    while True:
        exibir_menu()
        r = input('') 
        if r == '1':
            nome = input('Digite o nome do contato: ')
            telefone = input('Digite o telefone: ')
            adicionar_contato(agenda, nome, telefone)
        elif r == '2':
            nome = input('Digite o nome que queira excluir: ')
            excluir_contato(agenda, nome)
        elif r == '3':
            listar_contato(agenda, nome, telefone)
        elif r == '4':
            nome = input('Digite o nome do contato ')
            buscar_contato(agenda, nome)
        elif r == '5':
            print('Saindo...\n')
            break
        else:
            print('Opção inválida! Tente novamente.\n')

agenda_telefonica()