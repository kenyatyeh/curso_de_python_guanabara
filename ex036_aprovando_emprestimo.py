casa = float(input('Valor da casa: R$'))
salário = float(input('Saldo do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))
prestação = casa / (anos * 12)
mínimo = salário * 0.30
print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa, anos), end='')
print(' a prestação será de R${:.2f}'.format(prestação))
if prestação <= mínimo:
    print('Empréstimo \033[32mCONCEDIDO\033[m')
else:
    print('Emprestimo \033[31mNEGADO\033[m')
