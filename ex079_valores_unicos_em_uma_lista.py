lista = list()
while True:
    n= (int(input('Digite um valor: ')))
    if n not in lista:
        lista.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    r = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if r == 'N':
        break
lista.sort()
print(f'Você digitou os valores {lista}')