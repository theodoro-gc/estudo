soma = 0
cont = 0
for c in range(1, 7):
    numero = int(input('digite o {} valor  '. format(c)))
    if numero % 2 == 0:
        soma += numero
        cont += 0
print('você informou {} numeros PARES e a soma foi {} '.format(cont , soma))
