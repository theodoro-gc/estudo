numeroInteiro = int(input('Me diga um número inteiro: '))
print('''escolha uma das bases para a conversão
 [ 1 ] Binario
 [ 2 ] Octal
 [ 3 ] Hexadicimal''')
escolha = int(input('Sua escolha'))
if  escolha == 1:
    print('{} Convertido para binario é  {}'.format(numeroInteiro , bin(numeroInteiro)))
elif escolha == 2:
    print('{} Convertido para octal é {}'.format(numeroInteiro, oct(numeroInteiro)))
elif escolha == 3:
    print('{} Convertido para hexadecimal é {}'.format(numeroInteiro , hex(numeroInteiro)))
else:
    print('\033[0;31m Opcão invalida tente novamente')
