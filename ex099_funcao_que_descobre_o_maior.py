from random import randint
from time import sleep


def maior(* num):
    maior = cont = 0
    print('Analisando os valores passados...')
    for valor in num:
        print(f'{valor}', end=' ', flush=True) # Faz os parâmetros aparecerem 1 por 1
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f' Foram informados {cont} valores ao todo.')
    print(f'O maior valor encontrado foi {maior}.')
    print('-=' * 30)


# Programa principal
maior(randint(0, 10), randint(0, 10), randint(0, 10),
      randint(0, 10), randint(0, 10), randint(0, 10))
maior(randint(0, 10), randint(0, 10), randint(0, 10),
      randint(0, 10), randint(0, 10))
maior(randint(0, 10), randint(0, 10), randint(0, 10),
      randint(0, 10))
maior(randint(0, 10), randint(0, 10), randint(0, 10))
maior(randint(0, 10), randint(0, 10))
maior(randint(0, 10))
maior()
