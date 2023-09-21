from time import sleep


def contagem(ini, fim, pul):
    if pul < 0:
        pul *= -1  # *= muda o sinal para positivo -1 * -1 = 1 positivo
    if pul == 0:
        pul = 1
    print(f'Contagem de {ini} até {fim} de {pul} em {pul}: ')
    if ini < fim:
        cont = ini
        while cont <= fim:
            print(f'{cont} ', end='')
            cont += pul
            sleep(.25)
        print('FIM!')
        print('-=' * 20)
    else:
        cont = ini
        while cont >= fim:
            print(f'{cont} ', end='')
            cont -= pul
            sleep(.25)
        print('FIM!')
        print('-=' * 20)


# Programa principal
contagem(1, 10, 1)
contagem(10, 0, 2)
print('-=' * 20)
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Início: '))
fim = int(input('Fim: '))
pul = int(input('Passo: '))
print('-=' * 20)
contagem(ini, fim, pul)
