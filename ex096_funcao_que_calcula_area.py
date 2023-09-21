def titulo(txt):
    print('-' * 30)
    print(txt)
    print('-' * 30)


def mult(a, b):
    m = a * b
    print(f'A área de um terreno de {a:.1f} x {b:.1f} é de {m:.1f}m².')


titulo('Controle de Terrenos')
a = float(input('LARGURA (m): '))
b = float(input('COMPRIMENTO (m): '))
mult(a, b)