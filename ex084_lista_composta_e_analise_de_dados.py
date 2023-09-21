pessoas = []
dados = []
maior = menor = 0
while True:
    pessoas.append(str(input('Nome: ')).strip())
    pessoas.append(float(input('Peso: ')))
    if len(dados) == 0:
        maior = menor = pessoas[1]
    else:
        if pessoas[1] > maior:
            maior = pessoas[1]
        if pessoas[1] < menor:
            menor = pessoas[1]
    dados.append(pessoas[:])
    pessoas.clear()
    resp = ' '
    while resp not in 'SN':
        resp = str(input(('Quer continuar? [S/N] '))).upper().strip()[0]
    if resp == 'N':
        break
print(f'Ao todo foram cadastrados {len(dados)} pessoas.')
print(f'O maior peso foi de {maior}kg. Peso de ', end='')
for p in dados:
    if p[1] == maior:
        print(f'{p[0]}. ', end='')
print(f'\nO menor peso foi de {menor}kg. Peso de ', end='')
for p in dados:
    if p[1] == menor:
        print(f'{p[0]}. ', end='')