import random
import math
#ang = random.randint(1, 180)
ang = float(input('Digite o ângulo: '))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tg = math.tan(math.radians(ang))
print('ângulo = {}\nseno = {:.2f}\ncosseno = {:.2f}\ntangente = {:.2f}'.format(ang, sen, cos, tg))
