numeros = ('zero', 'um', 'dois', 'três', 'quatros', 'cinco', 'seis',
           'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
           'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito',
           'dezenove', 'vinte')
while True:
    n = int(input('Digite um número de 0 a 20: '))
    if 0 <= n <= 20:
        break
    print('Tente novamente. ', end='')
print(f'Você digitou o número {numeros[n]}')