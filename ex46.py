from datetime import  date
atualmente = date.today().year
nascimento = int(input('Ano de nascimento'))
idade = atualmente - nascimento
print('Quem nasceu em {} tem {} anos agora em {}'.format(nascimento ,idade ,atualmente ))
if idade == 18:
    print('você tem que alistar IMEDIATAMENTE!!!')
elif idade <  18:
    idade2 = idade - 18
    print('Ainda te falta {} anos para se alistar'.format(idade2))
elif idade > 18 :
    idade2 = idade - 18
    print('Você ja devia ter se alistado a {} anos!!!'.format(idade2))
