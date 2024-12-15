soma = contador = 0
while True:
    numeros = int(input('Digite um numero (999 para parar) :  '))
    if numeros == 999:
        break
    contador += 1
    soma += numeros
print(f'Você digitou {contador} numeros e a soma entre eles é de {soma}')
