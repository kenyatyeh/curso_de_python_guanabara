print('CÁLCULO DE TINTA PARA PAREDE')
l = float(input('Qual a largura da parede em metros? '))
h = float(input('Qual a altura da parede em metros? '))
a = h * l
t = a / 2
print('Para pintar a parede de {} m² será necessário {} L.'.format(a, t))
