from datetime import datetime
dados = dict()
dados['nome'] = str(input('Nome:  '))
nascimento = int(input('Ano de Nascimento:  '))
dados['idade'] = datetime.now().year - nascimento
dados['Carteira de trabalho'] = int(input('Carteira de trabalho: [0 se não tiver]:    '))
if dados['Carteira de trabalho'] != 0:
    dados['contratação'] = int(input('Ano de contratação:  '))
    dados['salario'] = float(input('Salario:  '))
    dados['Aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - datetime.now().year)
print('-=' * 30)
for k ,v in dados.items():
    print(f'  -{k} tem o valor {v}')