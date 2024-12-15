def area(larg, comp):
    soma = larg * comp
    print(f'A area de um terreno {largura}x{comprimento} é de {soma}m')


print('Calculador de Terrenos')
print('-='*20)
largura = float(input('LARGURA:  '))
comprimento = float(input('COMPRIMENTO:  '))
area(largura,comprimento)

