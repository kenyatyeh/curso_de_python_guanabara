from random import randint
from time import sleep
itens = ('PEDRA', 'PAPEL', 'TESOURA')
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
op = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('POOOO!')
sleep(1)
print('-=' * 10)
pc = randint(0, 2)
if op > 2:
    print('NÚMERO INVÁLIDO, TENTE NOVAMENTE.')
else:
    print('Você jogou {}'.format(itens[op]))
    print('O computador jogou {}'.format(itens[pc]))
print('-=' * 10)
if pc == 0:
    if op == 0:
        print('EMPATEEEE')
    elif op == 1:
        print('VOCÊ GANHOU!')
    elif op == 2:
        print('VOCÊ PERDEU!')
    else:
        print('JOGADA INVÁLIDA')
elif pc == 1:
    if op == 0:
        print('VOCÊ PERDEU!')
    elif op == 1:
        print('EMPATEEEE')
    elif op == 2:
        print('VOCÊ VENCEU!')
    else:
        print('JOGADA INVÁLIDA')
elif pc == 2:
    if op == 0:
        print('VOCÊ GANHOU!')
    elif op == 1:
        print('VOCÊ PERDEU!')
    elif op == 2:
        print('EMPATEEEE')
    else:
        print('JOGADA INVÁLIDA')