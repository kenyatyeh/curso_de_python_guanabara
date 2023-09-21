km = float(input('Km percorridos: '))
d = int(input('Dias de aluguel: '))
print('Valor a ser pago R${:.2f}.'.format((60 * d) + (.15 * km)))
