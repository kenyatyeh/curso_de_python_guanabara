from random import shuffle
n1 = str(input('1. '))
n2 = str(input('2. '))
n3 = str(input('3. '))
n4 = str(input('4. '))
lista = [n1, n2, n3, n4]
shuffle(lista)
print('Ordem de apresentação será:\n{}'.format(lista))
