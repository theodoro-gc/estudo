print('=' * 30)
print('{:^30}'.format('BANCO DISCO VOADOR'))
print('=' * 30)
valor = int(input('Quanto você quer sacar: '))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'O total de {totced} celulas de {ced} ')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced =10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break

