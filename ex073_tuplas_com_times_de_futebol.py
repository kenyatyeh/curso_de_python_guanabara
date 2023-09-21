tabela = ('Palmeiras', 'Internacional', 'Fluminense', 'Flamengo', 'Corinthians',
          'Athletico=PR', 'Atlético-MG', 'América-MG', 'Goiás, Botafogo',
          'Santos', 'Bragantino', 'São Pualo', 'Fortaleza', 'Ceará SC', 'Coritiba',
          'Avaí', 'Cuiabá', 'Atlético-GO', 'Juventude')
print('=' * 30)
print(f'Lista de times do Brasileirão {tabela}')
print('=' * 30)
print(f'Os 5 primeiros são {tabela[0:6]}')
print('=' * 30)
print(f'Os 4 últimos são {tabela[-4:]}')
print('=' * 30)
print(f'Times em ordem alfabética: {sorted(tabela)}')
print('=' * 30)
print('O Corinthians ficou na {}º posição'.format(tabela.index('Corinthians') + 1))

