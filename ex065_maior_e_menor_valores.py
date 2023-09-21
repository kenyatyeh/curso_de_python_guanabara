resp = 'Ss'
soma = quant = média = maior = menor = 0
while resp in 'Ss':
    n = int(input('Digite um número: '))
    soma += n
    quant += 1
    if quant == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
média = soma / quant
print('Você digitou {} números e a média foi {}'.format(quant, média))
print('O maior valor é {} e o menor é {}'.format(maior, menor))

