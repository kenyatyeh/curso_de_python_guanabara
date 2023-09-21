s = 0
c = 0
for n in range(1, 501, 2):
    if n % 3 == 0:
        c += 1
        s += n
print('A soma dos {} números impares múltiplos de 3 é {}'.format(c, s))
