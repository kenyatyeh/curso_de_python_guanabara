soma = produto1k = cont = menor = 0
barato = ''
while True:
    nome = str(input('Nome do produto: ')).strip()
    preco = float(input('Preço do produto: R$'))
    soma += preco
    cont += 1
    if preco > 1000.00:
        produto1k += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = nome
    resp = ' '
    while resp not in 'NS':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'TOTAL: R${soma:.2f}')
print(f'Temos {produto1k} produtos custando mais de R$1000,00')
print(f'O produto mais barato foi: {barato} que custa R${menor:.2f}')