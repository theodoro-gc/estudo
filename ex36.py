distancia = float(input('qual é a distancia da sua viagem'))
if distancia <= 200:
   preco = distancia * 0.50
   print('o preco da viagem é {} reais'.format(preco))
else:
    preco = distancia * 0.45
    print('o preco a pagar é {} reais '.format(preco))
print('você esta prestes de iniciar uma viagem de {}km'.format(distancia))