sal = float(input('Quanto ganha o funcionário: R$'))
if sal > 1250.00:
    print('Aumento de 10% -> R${:.2f}'.format(sal + (sal * 0.10)))
else:
    print('Aumento de 15% -> R${:.2f}'.format(sal + (sal * 0.15)))
