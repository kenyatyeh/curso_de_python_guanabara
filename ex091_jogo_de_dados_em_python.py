from random import  randint
from time import sleep
list = []
primeiro = segundo = nome1 = nome2 = 0
for c in range(0, 4):
    n = randint(1, 6)
    print(f'jogador{c + 1} tirou {n} no dado.')
    sleep(1)
    if c == 0:
        primeiro = segundo = n
        nome1 = nome2 = c + 1
    if n > primeiro:
        primeiro = n
        nome1 = c + 1
    elif n > segundo:
        segundo = n
        nome2 = c + 1
print('-='*30)
print(f'{"== RANKING DOS JOGADORES ==":^5}')
print(f' 1º lugar: jogador{nome1} com {primeiro}')
print(f' 2º lugar: jogador{nome2} com {segundo}')