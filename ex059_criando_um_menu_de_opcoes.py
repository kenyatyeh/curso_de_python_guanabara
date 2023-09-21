print('=-'*20)
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n = 0
while n != 5:
    print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    n = int(input('>>>>> Qual é a sua opção? '))
    if n == 1:
        s = n1 + n2
        print('O resultado de {} + {} é {}'.format(n1, n2, s))
    elif n == 2:
        m = n1 * n2
        print('O resultado de {} x {} é {}'.format(n1, n2, m))
    elif n == 3:
        if n1 > n2:
            print('Entre {} e {} o maior valor é {}'.format(n1, n2, n1))
        else:
            print('Entre {} e {} o maior número é {}'.format(n1, n2, n2))
    elif n == 4:
        print('Informe os números novamente:')
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))
print('Finalizando...')