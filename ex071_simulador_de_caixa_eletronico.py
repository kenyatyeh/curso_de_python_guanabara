print('=' * 30)
print('{:^30}'.format('BANCO MEU'))
print('=' * 30)
valor = int(input('Quanto você quer sacar?'))
total = valor
ced = 50
todced = 0
while True:
    if total >= ced:
        total -= ced
        todced += 1
    else:
        if todced > 0:
            print(f'Total de {todced} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        todced = 0
        if total == 0:
            break
print('=' * 30)
print('Volte Sempre!')
