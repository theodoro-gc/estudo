from  random import randint
from time import sleep


def sorteia(lista):
    print('Sorteando 5 valores da lista' , end=' ')
    for c in range(0,5):
                n = randint(0, 10)
                lista.append(n)
                print(f'{n} ',end=' ' , flush=True )
                sleep(0.3)
    print('Pronto')


def SomaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando`os valores pares de {lista}, Temos {soma}')


numeros = list()
sorteia(numeros)
SomaPar(numeros)
                 