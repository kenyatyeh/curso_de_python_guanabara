lista = []
cont = 0
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    cont += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break
lista.sort(reverse=True)
print(f'Você digitou {cont} elementos.')
print(f'Os valores em ordem decresecente são {lista}')
if 5 not in lista:
    print('O valor 5 não foi encontrado na lista!')
else:
    print('O valor 5 está na lista!')
