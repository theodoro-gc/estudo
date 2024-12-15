from time import  sleep


def maior(*num):
    cont = maior = 0
    print('-=' * 30)
    print('Analizando os valores passados... ')
    for valor in num:
        print(f'{valor} ',end=' ', flush=True)
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if  valor > maior:
                maior = valor
        cont += 1
    print(f'foram informados {cont} valores ao todo.  ')
    print(f'O maior valor informado foi {maior}.  ')


maior(2, 6  , 7, 8, 3, 9)
maior(3 , 7, 9)
maior(1, 5,)
maior()