print('\033[0;30;41m-=' * 15)
print('\033[0;30;41mCONVERSOR DE MOEDAS')
while True:
    print('-=' * 15)
    print('''\033[0;30;44m [1] Dolar Americano
 [2] Euro
 [3] Peso Argentino 
 [4] Yuan Chines     
 [5] sair''')
    print('-=' * 15)
    opcao = (input('\033[0;30;45mEscolha uma opção:  '))

    if opcao == '1':
        real = float(input('\033[0;30;43mQuanto dinheiro você tem nesse momento:  '))
        dolar = real / 5.65
        print(str(f'\033[0;30;46mCom R${real} você pode comprar {dolar:.2f} dolares'))
        resp = str(input('\033[0;30;42mQuer continuar? [S/N]:  ')).upper()
        while resp not in 'SN':
            resp = str(input('\033[0;30;42mQuer continuar? [S/N]:  ')).upper()
        if resp == 'N':
            break

    if opcao == '2':     
        real = float(input('\033[0;30;43mQuanto dinheiro você tem nesse momento:  '))
        euro = real / 6.13
        print(str(f'\033[0;30;46mCom R${real} você pode comprar {euro:.2f} euros'))     
        resp = str(input('\033[0;30;42mQuer continuar? [S/N]:  ')).upper()
        while resp not in 'SN':
            resp = str(input('\033[0;30;42mQuer continuar? [S/N]:  ')).upper()
        if resp == 'N':
            break

    if opcao == '3':
        real = float(input('\033[0;30;43mQuanto dinheiro você tem nesse momento:  '))
        Peso = real / 0.58
        print(str(f'\033[0;30;46mCom R${real} você pode comprar {Peso:.2f} pesos'))
        resp = str(input('\033[0;30;42mQuer continuar? [S/N]:  ')).upper()
        while resp not in 'SN':
            resp = str(input('\033[0;30;42mQuer continuar? [S/N]:  ')).upper()
        if resp == 'N':
            break

    if opcao == '4':
        real = float(input('\033[0;30;43mQuanto dinheiro você tem nesse momento:  '))
        yuan = real / 0.80
        print(str(f'\033[0;30;46mCom R${real} você pode comprar {yuan:.2f} yuan chines'))
        resp = str(input('\033[0;30;42mQuer continuar? [S/N]:  ')).upper()
        while resp not in 'SN':
            resp = str(input('\033[0;30;42mQuer continuar? [S/N]:  ')).upper()
        if resp == 'N':
            break

    if opcao == '5':
        print('\033[0;30;47mVolte sempre! ')
        break










