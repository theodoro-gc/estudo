nun1 = float(input('Digite um numero: '))
nun2 = float(input('Digite outro numero: '))
soma = nun1 +  nun2
divisaoDosNumeros = soma / 2
print('Tirando {} e {} , a media do aluno é {} '.format(nun1, nun2 , divisaoDosNumeros))
if divisaoDosNumeros <= 5:
    print('O auno esta reprovado REPROVADO HAAAAAAAAAAAA')
elif 7 > divisaoDosNumeros >= 5:
    print('O aluno esta de RECUPERAÇÃO anida da pra PASSARRRRR')
elif divisaoDosNumeros >= 7:
    print('O aluno esta APROVADO VIVAAAAAA')