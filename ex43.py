valorDaCasa = float(input('Digite um valor para a casa'))
salario = float(input('Digite o salario do funcionario'))
anosAPagar = int(input('Em quantos anos você vai pagar a casa'))
mesesAPagar = anosAPagar * 12
prestacaoMaxima = salario * 30 / 100
prestacaoDaCasa = valorDaCasa / mesesAPagar
if prestacaoDaCasa <= prestacaoMaxima:
    print('ENPRESTIMO PERMITIDO')
    print('todo mês você vai tem que pagar {:.2f} rais'.format(prestacaoDaCasa))
else:
    print('ENPRESTIMO NEGADO')

