from random import randint
computador = randint(1 , 10)
print('Heloo sou se computador, e acabei de pensar em um numero')
print('Se você não for burro você vai conceguir adivinhalo')
acerto = False
chute = 0
while not acerto:
    jogador = int(input('Qual é seu chute'))
    chute += 1
    if jogador == computador:
        acerto = True
    else:
        if jogador < computador:
            print('Mais Tente novamente')
        elif jogador > computador:
            print('Menos Tente novamente')
print('Parabens você acertou!! em {} tentaivas'.format(chute))