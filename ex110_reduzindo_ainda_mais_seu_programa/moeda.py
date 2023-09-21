def metade(n=0, formato=False):
    div = n / 2
    return div if formato is False else moeda(div)


def dobro(n=0, formato=False):
    dob = n * 2
    return dob if formato is False else moeda(dob)


def aumento(n=0, taxa=0, formato=False):
    '''
    -> Calcula o aumento de determinado preço
    retornando o resultado com ou sem formatação.
    :param n: o preço que se quer reajustar
    :param taxa: qual a porcentagem do aumento
    :param formato: quer a saída formatada ou não
    :return: o valor reajustado, com ou sem formato.
    '''
    aum = (n * taxa/100) + n
    return aum if not formato else moeda(aum)


def diminuir(n=0, taxa=0, formato=False):
    dim = n - (n * taxa/100)
    return dim if not formato else moeda(dim)


def moeda(n=0, moeda='R$'):
    return f'{moeda}{n:>.2f}'.replace('.', ',')


# replace irá substituir o . pela ,
# :8.2f = 8 casas decimais (00000000,00)
# \t -> tabulação


def resumo(n=0, taxaa= 10, taxar=5):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(n)}')
    print(f'Dobro do preço: \t{dobro(n, True)}')
    print(f'Metade do preço: \t{metade(n, True)}')
    print(f'{taxaa}% de aumento: \t{aumento(n, taxaa, True)}')
    print(f'{taxar}% de redução: \t{diminuir(n, taxar, True)}')
    print('-' * 30)
