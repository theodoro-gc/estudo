import time
from random import randint
v = 0
while True:
    jogador = (int(input('Digite um valor: ')))
    computador = randint(1 ,11)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PpIi':
        tipo = str(input('Par ou Impar [ P/I ]: ')).strip().upper()[0]
        print(f'Você jogou {jogador} dedos e o computador jogou {computador} \n O TOTAL É DE {total} ')
        if tipo == 'P':
            if total % 2 == 0:
                print('Voce venceu')
                v += 1
            else:
                print('voce perdeu')
                break
        elif tipo == 'I':
            if total % 2 == 1:
                print('voce venceu')
            else:
                print('voce perdeu ')
                break
print(f'É vpce venceu {v} veses')