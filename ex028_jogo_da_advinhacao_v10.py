from random import randint
from time import sleep
print('-='*50)
print('Vou pensar em um número entre 0 e 5. Tente advinhar.')
print('-='*52)
o = randint(0, 5)
n = int(input('Em que número eu pensei? ' ))
print('PROCESSANDO...')
sleep(3)
if n == o:
    print('ACERTOUUUU!')
else:
    print('EROUUUU')
print('Pensei no número: {}'.format(o))

