ficha = list()
while True:
    nome = str(input('Dite um nome:  '))
    nota1 = float(input('Nota 1:  '))
    nota2 = float(input('Nota 2:  '))
    print('-=' * 30)
    media = (nota1 + nota2 ) / 2
    ficha.append([nome, [nota1], [nota2] , media])
    resp = str(input('Quer continuar? [S/N]:  ')).upper()
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]:  ')).upper()
    if resp == 'N':
        break
for c in ficha:
    print(f'O {nome} teve a media de  {media}')
    print('-=' * 30)


resp2 = str(input('Gostaria de ver a nota de algum aluno especifico? [S/N]  ')).upper()

if resp2 == 'S':
    aluno = int(input('Qual é o numero do aluno desejado:  '))
    print(f'Notas de {ficha[int(aluno)][0]} foi {nota1} e {nota2}')
while resp2 not in 'SN':
    resp2 = str(input('Gostaria de ver a nota de algum aluno especifico? [S/N]:  ')).upper()
    if resp2 == 'N':
        break



