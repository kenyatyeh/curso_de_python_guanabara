matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
s = 0
mai2lin = matriz[1][0]
for l in range(0, 3):
    for c in range(0, 3):
        valor = int(input(f'Digite um valor [{l}, {c}]: '))
        matriz[l][c] = valor
        if valor % 2 == 0:
            s += valor
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
for c in range(0, 3):
    if c == 0:
        mai2lin = matriz[1][c]
    elif matriz[1][c] > mai2lin:
        mai2lin = matriz [1][c]
multcolu3 = matriz[0][2] + matriz[1][2] + matriz[2][2]
print('=-'*20)
print(f'A soma dos valores pares é {s}.')
print(f'A soma dos valores da terceira coluna é {multcolu3}.')
print(f'O maior valor da segunda linha é {mai2lin}.')
