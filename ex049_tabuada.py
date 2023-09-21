n = int(input('Escolha um número: '))
print('TABUADA DO {}'.format(n))
for t in range(1, 11):
    r = n * t
    print('{} x {} = {}'.format(n, t, r))

 #print('{} x {:2} = {}'.format(n, t, n*t))