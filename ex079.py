cont = ('zero' , 'um' , 'dois' , 'três' , 'quatro' ,
                    'cinco' , 'seis' , 'sete' , 'oito' , 'nove' ,
                    'dez' , 'onze' , 'doze' , 'treze' , 'catorze'
                    , 'quinze' , 'dezesseis' , 'dezessete' ,
                    'sezoito' , 'dezenove' , 'vinte')
while True:
    num = int(input('Digite um numero de 0 a 20:  '))
    if 0 <= num <= 20:
        break
    print('Tente novamente', end = ' ')
print(f'Você digitou o numero {cont [num] }')