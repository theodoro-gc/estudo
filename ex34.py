carro = int(input('escreva a velocidade do seu carro '))
if carro > 80:
    print('MUTADO! você passou o limite de velocidade')
    multa = carro * 7
    print('voce deve pagar uma multa de {:.2f} reais '.format(multa))
print('tenha um bom dia e direja com seguranssa')
