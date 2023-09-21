print('DETECTOR DE PALINDROME')
print('='*15)
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
print('A frase que você digitou foi {} e ela ao contrário é {}'.format(junto, junto[::-1]))
if junto == junto[::-1]:
    print('Esta frase é PALINDROME.')
else:
    print('NÃO É PALINDROME.')
print(len(junto) - 1, -1, -1)