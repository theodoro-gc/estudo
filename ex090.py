temp = []
princ = []
mai = men = 0
while True:
    temp.append(str(input('Digite seu nome:  ')))
    temp.append(int(input('Digite seu peso:  ')))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input('Quer continuar: [S/N] '))
    print('=-' * 30)
    if resp in 'Nn':
        break
print(f'Ao todo você cadastrou {len(princ)} pessoas')
print(f'O maior peso foi de {mai}Kg',end= ' ')
for p in princ:
    if p[1] == mai:
        print(f'[{p[0]}]')
print(f'O menor peso foi de {men}Kg',end= ' ')
for p in princ:
    if p[1] == men:
        print(f'[{p[0]}]')