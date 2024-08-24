'''variáveis'''
pi = 3.14


'''MENU'''
def menu():
    print('---MENU---')
    print('1. Cubo')
    print('2. Retângulo')
    print('3. Cilindro')
    print('4. Pirâmide')
    print('5. Sair')

'''CUBO'''
def cubo(a):
    return a ** 3

'''RETÂNGULO'''
def retangulo(B, L, h):
    return B * L * h

'''CILINDRO'''
def cilindro(pi, r, h):
    return pi * r ** 2 * h

'''PIRÂMIDE'''
def piramide(Ab, a, h):
    return (Ab / 1) * (h / 3)


'''CÓDIGO PRINCIPAL'''
def calculadora():
    while True:
        menu()
        resultado = input('Digite a opção desejada:\n')
        if resultado == '1':
            a = float(input('Digite o valor da ÁREA:\n'))
            volume = cubo(a)
            print(f'VOLUME = {volume:.2f}\n')
        
        if resultado == '2':
            B = float(input('Digite o valor da BASE:\n'))
            L = float(input('Digite o valor da LARGURA:\n'))
            h = float(input('Digite o valor da ALTURA:\n'))
            volume = retangulo(B, L, h)
            print(f'VOLUME = {volume:.2f}\n')

        if resultado == '3':
            r = float(input('Digite o valor do RAIO:\n'))
            h = float(input('Digite o valor da ALTURA:\n'))
            volume = cilindro(pi, r, h)
            print(f'VOLUME = {volume:.2f}\n')

        if resultado == '4':
            a = float(input('Digite o valor de um LADO da BASE:\n'))
            Ab = a ** 2
            h = float(input('Digite o valor da ALTURA:\n'))
            volume = piramide(Ab, a, h)
            print(f'VOLUME = {volume:.2f}\n')

        if resultado == '5':
            print('Saindo...')
            break

calculadora()