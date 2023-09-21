total = 0
cont = 0
n = int(input('Digite um número [999 para parar]: '))
while n != 999:
    total += n
    cont += 1
    n = int(input('Digite um número [999 para parar]: '))
print('Você digitou {} números e a soma entre eles foi  {}'.format(cont, total))