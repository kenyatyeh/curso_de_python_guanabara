def leiaInt(txt):
    ok = False
    valor = 0
    while True:
        n = str(input(txt))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033k'
                  '[m')
        if ok:
            break
    return valor


# Programa Principal
n = leiaInt('Digite um número: ')
print((f'Você acabou de digitar o número {n}'))