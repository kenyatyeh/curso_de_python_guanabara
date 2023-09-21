n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Mais um número: '))
# Verificando o maior
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
# Verificar o menor
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
print('O maior número: {}'.format(maior))
print('O menor valor: {}'. format(menor))
