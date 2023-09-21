valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'nN':
        break
print(f'Você digitou {len(valores)} elementos.')
valores.sort(reverse=True)
print(f'Os valores em ordem decresente são {valores}')
if 5 not in valores:
    print('O valor 5 não foi encontrado na lista!')
else:
    print('O valor 5 está na lista!')