from random import randint
print('-=' * 15)
nuns = (randint(1,10) , randint(1,10) , randint(1,10) , randint(1,10) , randint(1,10))
print(f'Os valores sorteador foram: {nuns}')
print('-=' * 15)
print(f'o maior valor sorteado foi {max(nuns)}')
print('-=' * 15)
print(f'o menor valor sorteado foi {min(nuns)}')
print('-=' * 15)