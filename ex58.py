soma = 0
caunt = 0
for c in range(1 , 7, ):
    numero = int(input('Digite um numero'))
    if numero % 2 == 0:
        soma += numero
        caunt += 1
print('voce informou {} numeros PARES e a soma entre eles foi de {}'.format(caunt, soma))




