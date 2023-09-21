#CONDIÇÃO COMPOSTA
v = int(input('Qual a velocidade atual do carro? '))
if v <= 80.0:
    print('Tenha um bom dia! Dirija com segurança!')
else:
    print('MULTADO! Você excedeu o limite permitido que é 80km/h')
    print('Você deve pagar uma multa de R${:.2f}!'.format(v * 7))
    print('Tenha um bom dia e dirija com segurança!')

#CONDIÇÃO SIMPLES
#if v > 80:
#    print('MULTADO! Você excedeu o limite permitido que é 80km/h')
#    print('Você deve pagar uma multa de R${:.2f}!'.format(v * 7))
#print('Tenha um bom dia e dirija com segurança!')