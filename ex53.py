from random import randint
itens = ('Pedra' , 'Papel' , 'Tesoura')
copiurer = randint (0 , 2)
print('''Suas opções: 
[ 0 ] Pedra
[ 1 ] Papel 
[ 2 ] Tesoura''')
player = int(input('qual sua jogada?:'))
print('o pleyer jogou {}'.format(itens [player]))
print('o computador jogou {}'.format(itens[copiurer]))

if copiurer == 0:

    if player == 0:
        print('Enpate')
    elif player == 1:
        print('jogador vence')
    elif player == 2:
        print('computador vence')
    else:
        print('raund invalido')

elif copiurer == 1:

    if player == 0:
        print('computador vence')
    elif player == 1:
        print('enpate')
    elif player == 2:
        print('jogador vence')
    else:
        print('raund invalido')

elif copiurer == 2:

    if player == 0:
        print('jogador vence')
    elif player == 1:
        print('computador vence')
    elif player == 2:
        print('enpate')
    else:
        print('raund invalido')
