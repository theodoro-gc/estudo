segmento1 = float(input('Primeiro seguimento: '))
segmento2 = float(input('Segundo seguimento: '))
segmento3  = float(input('Seguimento três: '))

if segmento1 == segmento2 and segmento1 == segmento3:
    print('Os seguimentos acima PODEM FORMAR um trialgulo EQILATERO :)')

elif segmento1 != segmento2 != segmento3 and segmento2 != segmento1 != segmento3 and segmento2 != segmento3:
    print('Os seguimentos acima PODEM FORMAR um triangulo ESCALENO ')

else:
    print('OS seguimentos acima  PODEM FORMAR um triangulo ISOSCELES')
