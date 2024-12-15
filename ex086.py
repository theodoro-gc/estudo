lista = list()
while True:
    n = (int(input(f'Digite um valor:  ')))
    if n not in lista:
        lista.append(n)
        print('valor adicionado com sucesso...')
    else:
        print('O numero ja foi adicionado tente novamente!')
    continuacao = (str(input('Quer continuar [N/S]:  '))).upper()[0]
    if continuacao in 'Nn':
        break
print(lista.sort())
print(f'Você digitou os valores {lista}')