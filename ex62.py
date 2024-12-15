
frase = str(input('digete uma frase: ')).strip().upper()
palavras = frase.split( )
juntando = ' '.join(palavras)
invertido = juntando[::-1]
print('O inverso da palavra {} é {} '.format(juntando , invertido))
if invertido == juntando:
    print('TEMOS UM PALINDROMO')
else:
    print(' a frase digitada nao é um palindromo')