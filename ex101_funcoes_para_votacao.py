from datetime import date


def voto(ano):
    print('-' * 30)
    nasc = int(input('Em que ano você nasceu? '))
    idade = date.today().year - nasc
    if idade < 16:
        print(f'Com {idade} anos: VOTO NEGADO.')
    elif idade == 16 or idade == 17:
        print(f'Com {idade} anos: VOTO OPCIONAL.')
    elif idade >= 70:
        print(f'Com {idade} anos: VOTO OPCIONAL.')
    else:
        print(f'Com {idade} anos: VOTO OBRIGATÓRIO.')


voto(1998)