import time
numero1 =int(input('Digite um valor: '))
numero2 =int(input('Digite outro valor: '))
opcao = 0
while opcao != 5:
    print('''[ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos numeros
    [ 5 ] Sair do programa''')
    opcao =int(input('qul é a sua opcao?'))
    if opcao == 1:
        soma = numero1 + numero2
        print('a soma entre {} e {} e de {}'.format(numero1 , numero2 ,soma ))
        print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')

    elif opcao == 2:
        multiplicassão = numero1 * numero2
        print('A multiplicasão entre {} e {} e de {}'.format(numero1 , numero2 , multiplicassão))
        print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')

    elif opcao == 3:
        print('Entre os numeros {} e {} o maior entre eles é {}'.format(numero1 , numero2 , max(numero1 , numero2)))
        print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')

    elif opcao == 4:
        print('Informe os numeros novamente porfavor')
        numero1 = (int(input('digite um numero: ')))
        numero2 = (int(input('digite um numero')))

    elif opcao == 5:
        print('Finalizando...')

    else:
        print('Opção invalida tente novamente')
        
    time.sleep(2)
print('Ate mais volte sempre')