s = cont = n = 0
while True:
    s += n
    cont += 1
    n = int(input('Digite um valor (999 para para): '))
    if n == 999:
        break
print(f'A soma dos {cont} valores foi {s}')