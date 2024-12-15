from random import randint
from time import sleep
lista = list()
jogos = list()
print('-='*30)
print('                     JOGO MEGA SENA')
print('-='*30)
quantos = int(input('Quantos jogos voce quer que eu sortei: '))
tot = 1
while tot <= quantos:
    cont = 0
    while True:
        nun = randint(1, 60)
        if nun not in lista:
            lista.append(nun)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-=' * 3 ,f'SORTEANDO {quantos} JOGOS','-='*3)
for i , l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print('-=' *30)
print('BOA SORTE')