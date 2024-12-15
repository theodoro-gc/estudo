valorDasCompras = float(input('Qual foi o valor das compras?: '))
print('''FORMAS DE PAGAMENTO
[ 1 ] Dinheiro / Cheque
[ 2 ] A vista no cartão
[ 3 ] em até 2x no cartão
[ 4 ] em até 3x no cartão''')
escolha = float(input('Qual é sua escolha?'))
if escolha == 1:
   total =  valorDasCompras - (valorDasCompras * 10 / 100)
   print('Sua compra de {} vai custar {} agora'.format(valorDasCompras, total))

elif escolha == 2:
    total = valorDasCompras - (valorDasCompras * 5 / 100)
    print('Sua compra de {} vai custar {} agora'.format(valorDasCompras, total))

elif escolha == 3:
   total = valorDasCompras
   parcela = total / 2
   print('Sua compra sera parcelada em 2x de {:.2f} '.format(parcela))

elif escolha == 4:
    total = valorDasCompras + (valorDasCompras * 20 / 100 )
    totaldeparcelas = int(input('Quantas parcela?: '))
    parcela = total / totaldeparcelas
    print('Sua compra sera parcelada em {}x de {}'.format(totaldeparcelas, parcela))
    print('Sua compra de {} reais vai custar {} reais no final'.format(valorDasCompras,total))
