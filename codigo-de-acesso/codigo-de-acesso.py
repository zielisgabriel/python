'''MENU'''
def menu():
    print('---MENU---')
    print('Olá, em que posso ajudar?')
    print('1. Criar um código de acesso')
    print('2. Alterar o código de acesso')
    print('3. Deletar o código de acesso')
    print('4. Sair')

'''CRIAR CÓDIGO'''
def criar_codigo(codigo, lista):
    if not lista:
        lista.append(codigo)
        print('Código de acesso criado com sucesso!')
    elif codigo in lista:
        print('Esse código já existe na lista, e não poderá adicionar mais de um código!')
    else:
        print('Já existe um código de acesso!')

'''ALTERAR CÓDIGO'''
def alterar_codigo(codigo, lista):
    '''
    >> OUTRA VERSÃO DE "if" <<
    if codigo in lista:
        print('Código verificado!')
        novo_codigo = input('Digite seu novo código:')
        lista[0] = novo_codigo
        print('Códgio Alterado com Sucesso!')
    '''
    
    if codigo in lista:
        print('Código verificado!')
        lista[0] = input('Digite seu novo código:')
    else:
        print('Alteração negada! Tente novamente.')

'''DELETAR CÓDIGO'''
def deletar_codigo(codigo, lista):
    if codigo in lista:
        del lista[0]
        print('Verificado, seu código foi excluido com sucesso!')
    else:
        print('Acesso negado, os código não coincidem')


'''CÓDIGO PRINCIPAL'''
def acesso():
    lista = []
    while True:
        menu()
        resposta = input('\nDigite sua opção:')
        if resposta == '1':
            codigo = input('Digite um código para acessar:')
            criar_codigo(codigo, lista)
        if resposta == '2':
            if not lista:
                codigo = input('Não existe código na lista, crie um agora:')
                lista.append(codigo)
            else:
                codigo = input('Para alterar o código, é preciso que você digite-o primeiro:')
                alterar_codigo(codigo, lista)
        if resposta == '3':
            if not lista:
                codigo = input('Não existe código na lista, crie um agora:')
                lista.append(codigo)
            else:
                codigo = input('Para deletar o código, é preciso que digite o código atual:')
                deletar_codigo(codigo, lista)
        if resposta == '4':
            print('Saindo...')
            break
acesso()