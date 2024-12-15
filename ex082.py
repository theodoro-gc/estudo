nun = (int(input( 'Digite um valor: ')),
            int(input( 'Digite outro valor:  ')),
            int(input( 'Digite mais um valor:  ')),
            int(input( 'Digite o ultimo valor:   ')))
print(f'Voce digitou os valores {nun}')
print(f'Voce digitou {nun.count(9)} veses o numero nove')
if 3 in nun:
    print(f'O valor 3 apareceu na {nun.index(3)+1}* posição')
else:
    print('o valor 3 NÃO foi digitado')
print(f'Os valores pares digitados foram')
for n in nun:
    if n % 2 == 0:
        print(n,  end=' ')