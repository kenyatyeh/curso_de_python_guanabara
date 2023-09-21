r1 = float(input('Lado 1: '))
r2 = float(input('Lado 2: '))
r3 = float(input('Lado 3: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    if r1 == r2 == r3:
        print('Triângulo EQUILÁTERO')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('Triângulo ISÓSCELES')
    else:
        print('Triângulo ESCALENO')
else:
    print('Não será possível formar um triângulo.')