print('GERADOR DE PA')
print('=-'*20)
pt = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
vezes = 1
pa = pt
while vezes <= 10:
    print('{} > '.format(pa), end='')
    pa += r
    vezes += 1
print('Fim')

