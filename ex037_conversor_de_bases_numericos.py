n = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases abaixo para fazer conversão:
[1] converter para BINÁRIO
[2] converter para OCTAL
[3] converter para HEXADECIMAL''')
choice = int(input('Sua opção: '))
if choice == 1:
    print('{} convertido para OCTAL é igual a {}'.format(n, bin(n)[2:]))
elif choice == 2:
    print('{} convertido para OCTAL é igual a {}'.format(n, oct(n)[2:]))
elif choice == 3:
    print('{} convertido para OCTAL é igual a {}'.format(n, hex(n)[2:]))
else:
    print('Número não identificado. Tente novamente.')