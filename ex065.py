sexo = str(input('Digite seu sexo [M/F]:  '))
while sexo not in 'MnFf':
    sexo = str(input('dados invalidos digite novamente')).strip().upper()[0]
print('sexo regitrado com sucesso!!')