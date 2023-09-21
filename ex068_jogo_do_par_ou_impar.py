from random import randint
print('-='*30)
print('VAMOS JOGAR PAR OU ÍMPAR')
conquistas = 0
while True:
    n = int(input('Diga um valor: '))
    escolha = str(input('Par ou ímpar? [P/I] ')).strip().upper()[0]
    print('-=' * 30)
    pc = randint(1, 10)
    soma = n + pc
    if soma % 2 == 0:
        print(f'Você jogou {n} e o computador {pc}. Total de {soma} DEU PAR')
        if escolha in 'P':
            print('VOCÊ VENCEU!')
            conquistas += 1
        else:
            print('VOCÊ PERDEU')
            break
    else:
        print(f'Você jogou {n} e o computador {pc}. Total de {soma} DEU ÍMPAR')
        if escolha in 'I':
            print('VOCÊ VENCEU!')
            conquistas += 1
        else:
            print('VOCÊ PERDEU')
            break
print('-=' * 30)
print(f'GAME OVER! Você venceu {conquistas} vezes.')