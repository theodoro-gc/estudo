soma = contador = numero = 0
numero = int(input('digite um numero [ Digite 999 pra parar]'))
while numero != 999:
    contador += 1
    soma += numero
    numero = int(input('digite um numero [ Digite 999 pra parar]'))

print (str('Voce digitou {} numeros e a soma entre eles foi de {}'.format(contador, soma)))
print('Acabou')