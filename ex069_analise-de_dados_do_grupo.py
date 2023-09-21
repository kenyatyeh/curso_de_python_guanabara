print('CADASTRO')
print('~' * 30)
pessoas18 = homens = mulheres20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [F/M] ')).upper().strip()[0]
    if idade >= 18:
        pessoas18 += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres20 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
        if resp in 'Nn':
            break
print('~' * 30)
print(f'{pessoas18} pessoas possuem mais de 18 anos.')
print(f'Foram cadastrados {homens} homens')
print(f'{mulheres20} mulheres têm menos de 20 anos')
print('Cadastro ENCERRADO.')