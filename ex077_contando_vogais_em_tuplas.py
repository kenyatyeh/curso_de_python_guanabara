palavras = ('comer', 'praticar', 'nadar', 'vender', 'estudar',
            'conversar', 'amar', 'brincar', 'ser', 'malhar',
            'trabalhar', 'enxergar', 'sentir', 'cheirar')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')