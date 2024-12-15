jogador = dict()
partidas = list()
jogador['nome'] = str(input('Nome do jogador:  '))
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou?  '))
for c in range(0 , tot):
    partidas.append(int(input(f'Quantos gols na partida {c + 1}:  ' )))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('-=' * 30)
print(jogador)
print('-=' * 30)
print(f'O campo nome tem o valor {jogador["nome"]} ')
print(f'O campo gols tem o valor {jogador["gols"]} ')
print(f'O campo total tem o valor {jogador["total"]} ')
print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {partidas[0]} jogos')

for k, v in enumerate(jogador["gols"]):
    print(f'Na partida {k + 1}, fez {partidas[k]} gols')
print(f'Foi um total de {jogador["total"]} gols')

