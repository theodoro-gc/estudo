import random
num =int(input('o computador pensou em um numero entre 0 e 5 você consegue adivinhar o numero?'))
sorteio = random.randint(0,5)
if num == sorteio:
    print('parabens o numero pensado pelo conputador foi {} o mesmo que o seu você ganhou!'.format(num))
else:
    print('o numero pensado pelo computador nao foi o mesmo que o seu você perdeu!')