nun = [[] , [] ]
valor = 0
for c in range(1, 8):
    valor = int(input(f'Digite um valor na {c}.posição:  '))
    if valor % 2 == 0:
        nun[0].append(valor)
    elif valor % 2 == 1:
        nun[1].append(valor)
print('=-' * 30)
nun[0].sort()
nun[1].sort()
print(f'Os numeros pares forão {nun[0]} ')
print(f'Os numeros impares forão {nun[1]} ')