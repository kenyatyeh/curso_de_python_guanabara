print('TERMOS DE UMA PA')
print('='*20)
t = int(input('Primeiro termo: ')) # número que dará o início
r = int(input('Razão: ')) # a razão vai ser o pula em pula
d = t + (10 - 1) * r # décimo termo, que  matemática diz que é o énesimo termo de uma PA
for c in range(t, d, r):
    print('{}'.format(c), end=' -> ')
print('Acabou')