p = float(input('Valor do produto R$'))
print('''Escolha uma das opções abaixo:
[1]à vista dinheiro/cheque: 10% de desconto
[2]à vista no cartão: 5% de desconto
[3]em até 2x no cartão: preço formal 
[4]3x ou mais no cartão: 20% de juros''')
op = int(input('Opção: '))
if op == 1:
    print('Preço a ser pago: R${:.2f}'.format(p - (p * 0.10)))
elif op == 2:
    print('Preço a ser pago: R${:.2f}'.format(p - (p * 0.05)))
elif op == 3:
    print('Preço a ser pago: R${:.2f}'.format(p))
elif op == 4:
    print('Preço a ser pago: R${:.2f}'.format(p + (p * 0.20)))
else:
    print('Opção inválida, tente novamente.')