aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Média do aluno {aluno["nome"]}: '))
if aluno['media'] >= 7:
    aluno['situacao'] = 'Aluno APROVADO'
elif aluno['media'] <= 5:
    aluno['situacao'] = 'Aluno REPROVADO'
elif aluno['media'] >= 6:
    aluno['situacao'] = 'Aluno de RECUPERAÇÃO'
print('-'*30)
for k, v in aluno.items():
    print(f'- {k} é igual a {v}')
