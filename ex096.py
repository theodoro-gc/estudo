dic = {'nome': str(input('Digite um nome:  '))}
dic2 = {'media':float(input(f'media de {dic["nome"]}:  '))}
print(f'Nome é igual á {dic["nome"]} ')
print(f'Media é igual á {dic2["media"]}')
media = 0
if media <= 5:
    print('A situação é igual á reprovado')
elif media >= 6:
    print('A situação é igual á aprovado')