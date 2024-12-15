Peso = float(input('Qual é seu peso em (KG): '))
Altura = float(input('Qual é sua altura: '))
imc = Peso / (Altura * Altura)
print('O imc dessa pessoa é de {:.1f}'.format(imc))
if imc <= 18.5:
    print('Você abaixo do peso ideal!')
elif imc <= 25:
    print('Você esta no peso ideal')
elif imc <= 30:
    print('Você esta com sobre peso!')
elif imc <= 40:
    print('Você esta com OBESIDADE!!')
else:
    print('Você esta com OBESIDADE MORBIA')