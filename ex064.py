pesoMaximo = 0
pesoMinimo = 0
for gordura in range(1, 6):
    peso = float(input('peso da {}* pessoa: '.format(gordura)))
    if gordura == 1:
        pesoMaximo = peso
        pesoMinimo = peso
    else:
        if peso > pesoMaximo:
            pesoMaximo = peso
        if peso < pesoMinimo:
            pesoMinimo = peso
print('o peso mais alto escrito foi de {}'.format(pesoMaximo))
print('o peso mais baixo escrito foi de {}'.format(pesoMinimo))
