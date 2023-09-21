lista = []
par = []
impar = []
while True:
    n = (int(input('Digite um número: ')))
    lista.append(n)
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break
print(f'A lista completa é {lista}')
print(f'A lista de pares é {par}')
print(f'A lista de ímpares é {impar}')
