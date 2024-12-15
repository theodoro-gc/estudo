from datetime import date
tototalMaior = 0
totalMenor = 0
atualmente = date.today().year
for pessoas in range(1, 8):
    nacimento = int(input('em que ano a {}* pessoa nasceu'.format(pessoas)))
    idade = atualmente - nacimento
    if idade >= 21:
        tototalMaior += 1
    else:
        totalMenor += 1
print('pelas datas informadas {} sao de maior'.format(tototalMaior))
print('pelas datas informadas {} sao de menor'.format(totalMenor))
