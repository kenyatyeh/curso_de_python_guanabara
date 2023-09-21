from datetime import date
totalmenor = 0
totalmaior = 0
atual = date.today().year
for c in range(1, 8):
    ano = int(input('Em que ano a {}º pessoa nasceu?'.format(c)))
    idade = atual - ano
    if idade <= 21:
        totalmenor += 1
    else:
        totalmaior += 1
print('{} pessoas são menores de idade.'.format(totalmenor))
print('{} pessoas já atingiram a maioridade.'.format(totalmaior))
