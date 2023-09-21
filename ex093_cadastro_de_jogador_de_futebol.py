dados = {}
lista = []
dados['nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
for v in range(0, partidas):
    lista.append(int(input(f'Quantos gols na partida {v}? ')))
dados['gols'] = lista[:] # Não esquecer [:] se não dá problema
dados['total'] = sum(lista)
print('-=' * 30)
print(dados)
print('-=' * 30)
for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {dados["nome"]} jogou {len(lista)} partidas.')
for i, n in enumerate(lista):
    print(f'   => N a partida {i}, fez {n} gols.')
print(f'Foi um total de {dados["total"]} gols.')