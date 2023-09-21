n = int(input('Digite um Número: '))
print('Número {}'.format(n))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))
c1 = n / 100
c2 = n // 100
c3 = n // 100 % 1
c4 = n // 100 % 10
print(c1)
print(c2)
print(c3)
print(c4)

