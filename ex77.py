print('-' * 37)
print('MERCADO DO COTOCO')
print('-' * 37)
total = tot1000 = menor = contador = 0
barato = ' '
while True:
    prodNome = str(input('Nome do produto:  '))
    preco = int(input('Preço:  '))
    total += preco
    contador += 1
    resposta = ' '
    if preco > 1000:
        tot1000 += 1

    if contador == 1 or preco < menor:
        menor = preco
        barato = prodNome

    else:
        if preco < menor:
            menor = preco


    while resposta not in 'SN':
        resposta = str(input('Quer continuar?:  ')).strip().upper()[0]
    if resposta == 'N':
        break
print(f'O total da compra foi de {total} RS')
print(f'{tot1000} Produtos custão mais de 1000 reais')
print(f'O produto mais barato foi {barato} que  custa RS{menor:.2f}')