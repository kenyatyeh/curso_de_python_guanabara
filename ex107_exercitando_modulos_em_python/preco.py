from ex107 import moeda
# Programa Principal
p = float(input('Digite o preço: R$'))
print(f'A metade de R${p:.1f} é R${moeda.metade(p)}')
print(f'O dobro de R${p:.1f} é R${moeda.dobro(p)}')
print(f'Aumentando 10%, temos R${moeda.aumento(p, 10)}')
print(f'Diminuindo 10%, temos R${moeda.diminuir(p, 10)}')