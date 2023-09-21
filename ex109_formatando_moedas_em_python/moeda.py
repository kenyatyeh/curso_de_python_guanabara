def metade(n=0, formato=False):
    div = n / 2
    return div if formato is False else moeda(div)


def dobro(n=0, formato=False):
    dob = n * 2
    return dob if formato is False else moeda(dob)


def aumento(n=0, taxa=0, formato=False):
    aum = (n * taxa/100) + n
    return aum if not formato else moeda(aum)


def diminuir(n=0, taxa=0, formato=False):
    dim = n - (n * taxa/100)
    return dim if not formato else moeda(dim)


def moeda(n=0, moeda='R$'):
    return f'{moeda}{n:>.2f}'.replace('.', ',')


# replace irá substituir o . pela ,
# :8.2f = 8 casas decimais (00000000,00)