from datetime import date
ano = int(input('Ano de nascimento: '))
atual = date.today().year
idade = atual - ano
print('Você nasceu em {} então tem {} anos.'. format(ano, idade))
if idade == 18:
    print('Você deve se alistar já, pois atingiu a maioridade este ano.')
elif idade < 18:
    saldo = 18 - idade
    print('Espere completar a maioridade daquia a {} anos, para se alistar no exército.'.format(saldo))
else:
    saldo = idade - 18
    print('Já passou do tempo de se alistar. Foi a {} anos atrás.'.format(saldo))