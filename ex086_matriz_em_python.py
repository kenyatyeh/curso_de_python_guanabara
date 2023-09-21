tot = [[], [], []]
for p in range(0, 3):
    tot[0].append(int(input(f'Digite um valor para [0, {p}]: ')))
for p in range(0, 3):
    tot[1].append(int(input(f'Digite um valor para [1, {p}]: ')))
for p in range(0, 3):
    tot[2].append(int(input(f'Digite um valor para [2, {p}]: ')))
print('-='*30)
for p in tot[0]:
    print(f'[{p:^5}]', end=' ')
print()
for p in tot[1]:
    print(f'[{p:^5}]', end=' ')
print()
for p in tot[2]:
    print(f'[{p:^5}]', end=' ')
print()
