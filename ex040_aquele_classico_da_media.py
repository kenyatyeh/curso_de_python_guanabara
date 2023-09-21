n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
m = (n1 + n2) / 2
print('A média do aluno é {:.1f}'.format(m))
if m < 5.0:
    print('O aluno está de \033[1;31mREPROVADO\033[m.')
elif 7 > m >= 5:
    print('O aluno esta de \033[1;33mRECUPERAÇÃO\033[m.')
elif m >= 7:
    print('Aluno \033[1;32mAPROVADO\033[m.')