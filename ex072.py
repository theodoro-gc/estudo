numero = 0
receptor = 's'
soma = 0
while receptor ==  's':
    numero = int(input('Digite um numero:  '))
    soma += numero
    receptor = str(input('Quer continuar [S/N]:  ')).lower()
    while (receptor != 's' and receptor != 'n'):
        receptor = str(input('Quer continuar [S/N]:  ')).lower()
print('o maior numero digitado foi {}'.format(max(numero)))
print('A soma dos valores digitados é  '+str(soma))
print('Volte Sempre')
