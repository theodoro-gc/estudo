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
    print('=-' * 30)
print('=-' * 30)
if 5 in lista:
    print('A lista tem o valor 5 ')
else:
    print('A lista não tem o valor 5')

(lista.sort(reverse=True))
print(f'a lista em ordem decresente é {lista}')
print(f'A lista tem {len(lista)} elementos')