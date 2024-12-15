salarioDoFuncionario = float(input('Qual o salario do funcionario'))
if salarioDoFuncionario <= 1250:
    aumento = salarioDoFuncionario * 0.10
    dinhero = salarioDoFuncionario + aumento
    print('Agora o funcionario vai ganhar vai ganhar {} reais'.format(dinhero))
else:
    aumento = salarioDoFuncionario * 0.15
    dinheiro = salarioDoFuncionario + aumento
    print('Agora o funcionario vai ganhar {} reais'.format(dinheiro))
