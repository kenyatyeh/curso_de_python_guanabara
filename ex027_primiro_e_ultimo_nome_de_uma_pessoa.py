n = str(input('Enter your full name: ')).strip()
nome = n.split()
print('Your first name is {}'.format(nome[0]))
print('Your last name is {}'.format(nome[len(nome)-1]))
