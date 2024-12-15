pessoa = dict()
pessoas = list()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome:  '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F]:  ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO porfavor digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade:  '))
    soma += pessoa['idade']
    pessoas.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar:  ')).upper()
        if resp in 'SN':
            break
        print('ERRO Digite apenas S ou N: ')
    if resp == 'N':
            break
    print('-=' * 30)
print('-=' * 30)
print(f'A o todo temos {len(pessoas)} pessoas cadastradas')
media = soma / len(pessoas)
print(f'A media de idade é de {media:5.2f} anos')
print('As mulheres cadastradas foram',end=' ')
for p in pessoas:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]}',end=' ')
print()
print('D) lista das pessoas que estão acima da media:  ',end=' ')
for p in pessoas:
    if p['idade'] >= media:
        print(' ')
        for k ,v in p.items():
            print(f'{k} = {v}', end=' ')
        print()
print('<< ENCERADO')