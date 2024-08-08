def calculadora():
    while True:
        op = str(input('Digite a operação:\n'))
        n1 = float(input('Digite um número:\n'))
        n2 = float(input('Digite outro número:\n'))

        if op == '+':
            r = n1 + n2
            print ('Resultado: %.2f %s %.2f = %.2f' % (n1, op, n2, r))
        if op == '-':
            r = n1 - n2
            print ('Resultado: %.2f %s %.2f = %.2f' % (n1, op, n2, r))
        if op == '*':
            r = n1 * n2
            print ('Resultado: %.2f %s %.2f = %.2f' % (n1, op, n2, r))
        if op == '/':
            if n2 == 0:
                print ('Nenhum número é divisível por 0')
            else:
                r = n1 / n2
                print ('Resultado: %.2f %s %.2f = %.2f' % (n1, op, n2, r))

            outra_operacao = input('\nQuer fazer outra operação?\n1.Sim\n2.Não\n')
            if outra_operacao == '2':
                print('Saindo')
                break

calculadora()