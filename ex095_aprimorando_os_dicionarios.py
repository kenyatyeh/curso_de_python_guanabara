pessoa = {}
gols = []
galera = []
while True:
    pessoa['nome'] = str(input('Nome do Jogador: '))
    n = int(input(f'Quantas partidas o {pessoa["nome"]} jogou? '))
    for g in range(0, n):
        gols.append(int(input(f'  Quantas gols na partida {g + 1}? ')))
        pessoa['gols'] = gols[:]
        pessoa['total'] = sum(gols)
    galera.append(pessoa.copy())
    gols.clear()
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
        if resp in 'SN':
            break
        print('Responda apenas S ou N.')
    if resp == 'N':
        break
print('-=' * 30)
print(f'cod ', end='')
for k in pessoa.keys():
    print(f'{k:<15}', end='')
print()
print('-' * 40)
for i, p in enumerate(galera):
    print(f'{i:>3} ', end='')
    for d in p.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar): '))
    if busca == 999:
        break
    if busca>= len(galera):
        print(f'ERRO! Não existe jogador com código {busca}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {galera[busca]["nome"]}: ')
        for i, g in enumerate(galera[busca]['gols']):
            print(f'    No jogo {i + 1} fez {g} gols.')
    print('-' * 40)
print('<<VOLTE SEMPRE!>>')