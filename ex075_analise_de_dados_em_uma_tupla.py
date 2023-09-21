n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))
n4 = int(input('Digite o último número: '))
tupla = (n1, n2, n3, n4)

n = (int(input('Digite um número: ')), # Já cria direto uma tupla
    int(input('Digite outro número: ')),
    int(input('Digite mais um número: ')),
    int(input('Digite o último número: ')))

print(f'O valor 9 apareceu {tupla.count(9)} vezes')
if 3 in tupla:
    print(f'O valor 3 apareceu na {tupla.index(3)+1}º posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
cont = 0
for c in tupla:
    if c % 2 == 0:
        cont += 1
print(f'Os valores pares digitados foram {cont}')