def metade(n=0):
    div = n / 2
    return div


def dobro(n=0):
    dob = n * 2
    return dob


def aumento(n=0, taxa=0):
    aum = (n * taxa/100) + n
    return aum


def diminuir(n=0, taxa=0):
    dim = n - (n * taxa/100)
    return dim


def moeda(n=0, moeda='R$'):
    return f'{moeda}{n:>.2f}'.replace('.', ',')


# replace irá substituir o . pela ,
# :8.2f = 8 casas decimais (00000000,00)