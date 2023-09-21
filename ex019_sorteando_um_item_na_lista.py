import random
a1 = str(input('1. '))
a2 = str(input('2. '))
a3 = str(input('3. '))
a4 = str(input('4. '))
lista = [a1, a2, a3, a4]
escolhido = random.choice(lista)
print('Escolhido: {}'.format(escolhido))