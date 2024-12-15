nun = list()
pares = list()
impares = list()
while True:
    nun.append(int(input('Digite um numero:  ')))
    resposta = str(input('Quer continuar: [S/N]  '))
    if resposta in 'Nn':
        break
for i , v in enumerate(nun):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
print('=-' * 30)
print(f'A lista completa {nun}')
print(f'A lista só com os numeros pares {pares}')
print(f'A lista só com os numeros impares {impares}')