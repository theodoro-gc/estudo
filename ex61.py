numero = int(input('digite um numero'))
tot = 0
for c in range(1 , numero + 1 ):
    if numero % c == 0:
        tot += 1
    else:
        print('{}'.format(c) )
print('O numero {}  foi  divisivel {} veses'.format(numero , tot))
if  tot == 2:
    print('E por causa disso ele é um numero primo')
else:
    print('E por causa disso ele não é um numero primo')