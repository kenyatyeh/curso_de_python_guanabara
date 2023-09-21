pessoa = {}
lista = []
ranking = []
soma = 0
while True:
    pessoa['nome'] = str(input('Nome: '))
    pessoa['sexo'] = str(input('Sexo: [F/M] ')).strip().upper()[0]
   while  pessoa['sexo'] not in 'FM':
        print('ERRO! Por favor, digite apenas M ou F.')
        pessoa['sexo'] = str(input('Sexo: [F/M] ')).strip().upper()[0]
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    lista.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
media = soma / len(lista)
print('-=' * 30)
print(f'A) Ao todo temos {len(lista)} pessoas cadastradas.')
print(f'B) A média de idade é de {media:.2f} anos.')
print(f'C) As mulheres cadastradas foram ', end='')
for p in lista:
    if p['sexo'] in 'F':
        print(f'{p["nome"]} ', end='')
print()
print(f'D) As pessoas que estão acima da média: ')
for p in lista:
    if p['idade'] >= media:
        print('     ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<<ENCERRADO>>')
