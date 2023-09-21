def voto(ano):
    from datetime import date
    print('-' * 30)
    idade = date.today().year - nasc
    if idade < 16:
        return f'Com {idade} anos: VOTO NEGADO.'
    elif 16 <= idade < 18 or idade >= 70:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'


# Programa Principal
nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))