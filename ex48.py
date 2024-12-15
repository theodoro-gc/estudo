from datetime import date
atualmente =date.today( ).year
nacimento = int(input('Ano do seu nascimento: '))
idade = atualmente - nacimento
print('O atleta tem {} anos'.format(idade))
if idade <= 9:
    print('CLASSIFICASÃO MERIN')
elif idade <= 14:
    print('CALSSIFICASÃO INFANTIL')
elif idade <=  19:
    print('CLASSIFICASÃO JUNIOR')
elif idade <= 25:
    print('CLASSIFICASÃO SENIOR')
else:
    print('CLASSIFICASÃO MASTER')