lista = []
par = []
impar = []
while True:
    n = (int(input('Digite um número: ')))
    lista.append(n)
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break
for i, n in enumerate(lista):
    if n % 2 == 0:
        par.append(n)
    elif n % 2 == 1:
        impar.append(n)
print(f'A lista completa é {lista}')
print(f'A lista de pares é {par}')
print(f'A lista de ímpares é {impar}')