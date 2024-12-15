while True:
    tabuada = int(input("Tabuada do numero: "))
    if tabuada < 0:
        break
    for count in range(1 , 11):
        print(f'{tabuada} x {count} = {tabuada * count}')
print('Programa de tabuada encerado')