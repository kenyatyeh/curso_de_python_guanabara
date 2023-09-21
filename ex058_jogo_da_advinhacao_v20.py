from random import randint
npc = randint(0, 10)
n = int(input('Advinhe o número que estou pensando de 0 a 10: '))
while n != npc:
    n = int(input('Ainda não, tente de novo: '))
print('VOCÊ CONSEGUIUUUUUU!!! O número que pensei foi {}'.format(npc))

