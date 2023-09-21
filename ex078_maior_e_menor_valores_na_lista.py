valores = list()
for c in range(0, 5):
    valores.append(int(input(f'Digite um valor para a Posição {c}: ')))
print(f'Você digitou os valores {valores}')
print(f'O maior valor digitado foi {max(valores)} na posição', end=' ')
for i, v in enumerate(valores):
    if v == max(valores):
        print(f'{i}...', end=' ')
print(f'\nO menor valor digitado foi {min(valores)} na posição', end=' ')
for i, v in enumerate(valores): # Enumerete pega tanto a posição quanto valor
    if v == min(valores):
        print(f'{i}...', end=' ')