listaDeNumeros = []
for c in range(1,5):
    listaDeNumeros.append(int(input(f'Digite um valor na posição {c}  ')))
print('=-' * 20)
print(f'o maior valor digitado foi {max(listaDeNumeros)}')
print(f'Na posição {listaDeNumeros.index(max(listaDeNumeros))+1}')
print('=-' * 20)
print(f'o menor numero digitado foi {min(listaDeNumeros)}')
print(f'Na posição {listaDeNumeros.index(min(listaDeNumeros))+1}')
print(listaDeNumeros)

