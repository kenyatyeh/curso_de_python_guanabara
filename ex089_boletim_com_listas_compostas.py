lista = []
while True:
    nome = (str(input('Nome: ')).strip())
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    m = (n1 + n2) / 2
    lista.append([nome, [n1, n2], m])
    resp = ' '
    while resp not in 'S/N':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
for i, a in enumerate(lista):
    print(f'{i:<4}{a[0]:<10}{a[2]:8.1f}')
while True:
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(lista) - 1:
        print(f'Notas de {lista[opc][0]} são {lista[opc][1]}')