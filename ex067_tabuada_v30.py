while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    if n < 0 or n == 0:
        break
    print('-' * 30)
    for c in range(1, 11):
        print(f'{n} x {c} = {n*c}')
    print('-'*30)
print('Programa de Tabuada ENCERRADO. Obrigado e volte sempre!')
