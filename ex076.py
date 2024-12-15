print('-=--=--=--=--=--=-CADASTRE-SE-=--=--=--=--=--=--=')
tot18 =toth = totm20 = 0
while True:
    idade = int(input('Idade:  '))
    sexo = '  '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]:  ')).strip().upper()[0]
        if idade >= 18:
            tot18 += 1
        if sexo == 'M':
            toth += 1
        if sexo == 'F' and idade < 20:
            totm20 += 1
    resposta = '  '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar?:  ')).strip().upper()[0]
    if resposta == 'N':
            break
print(f'{tot18} pessoas tem mais de 18 anos')
print(f'{toth} homens foram cadastrados')
print(f'{totm20} mulheres tem menos  de 20 anos')

