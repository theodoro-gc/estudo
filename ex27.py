numero = str(input('digite um numero'))
partes = numero.split(',')
resultado = max(partes, key=len)

print('o maior numero é {}'.format(resultado))
