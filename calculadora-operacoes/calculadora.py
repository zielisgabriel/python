'''Adição'''
def soma(x, y):
    return x + y

'''Subtração'''
def subtracao(x, y):
    return x - y

'''Divisão'''
def divisao(x, y):
    if y == 0:
        print('Nenhum número é divisível por 0')
    else:
        return x / y
    
'''Multiplicação'''
def multiplicar(x, y):
    return x * y

'''Menu'''
def menu():
    print ('---MENU---')
    print ('1. Adição')
    print ('2. Subtração')
    print ('3. Multiplicação')
    print ('4. Divisão')
    print ('5. Sair')


'''CÓDIGO PRINCIPAL'''
def calculadora():
    while True:
        menu()
        resposta = input('\nDigite a opção desejada:\n')
        num1 = float(input('Digite um número:\n'))
        num2 = float(input('Digite outro número:\n'))

        if resposta == '1':
            print(f'{num1} + {num2} = {soma(num1, num2)}\n')

        if resposta == '2':
            print(f'{num1} - {num2} = {subtracao(num1, num2)}\n')
        
        if resposta == '3':
            print(f'{num1} * {num2} = {multiplicar(num1, num2)}\n')

        if resposta == '4':
            print(f'{num1} / {num2} = {divisao(num1, num2)}\n')

        if resposta == '5':
            print('Saindo...')
            break
            
        else:
            print('Opção inválida!\n')
calculadora()