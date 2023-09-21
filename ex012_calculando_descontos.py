print('5% DO PRODUTO')
p = float(input('Digite o preço do produto: '))
d = p - (p * 0.05)
print('O desconto de 5% de R${:.2f} será de R${:.2f}'.format(p, d))
