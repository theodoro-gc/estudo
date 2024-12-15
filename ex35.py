numero =int(input('digite qualquer numero'))
resuntado = numero % 2
if resuntado == 0:
    print('o numero {} é par'.format(numero))
else:
    print('o numero {} é impar'.format(numero))