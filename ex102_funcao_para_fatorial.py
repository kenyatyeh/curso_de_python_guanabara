def fatorial(n, show=False):
    '''
    -> CALCULA O FATORIAL DE UM NÚMERO
    :param n: O número a ser calculado.
    :param show: (opicional) mostrar ou não a conta.
    :return: O valor do Fatorial de um número n.
    '''
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


# Programa Principal
print(fatorial(5, show=True))
print(fatorial(5, show=False))
print('-' * 50)
help(fatorial)