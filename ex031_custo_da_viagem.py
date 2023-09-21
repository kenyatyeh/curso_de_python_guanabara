km = int(input('Qual a distância da sua viagem? '))
if km <= 200:
    print('O preço da viagem será R${:.2f}'.format(km * 0.50))
else:
    print('O preço da viagem será R${:.2f}'.format(km * 0.45))

#CONDIÇÃO SIMPLIFICADA
#preço = km + 0.50 if km <= 200 else km * 0.45
#print('O preço da viagem será R${:.2f}'.format(preço))