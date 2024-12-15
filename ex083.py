print('-=' * 20)
print('                         LOLJINHA')
print('-=' * 20)

lista = ('lapis' , 1.75,
              'caderno' , 4.35,
              'caneta' , 2.12 ,
              'borracha' , 1.50,
               'livro' , 6.70,
               'estojo' , 4.20,
               'mochila' , 19.20,)
for pos in range(0 , len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}' , end=' ')
    else:
        print(f'{lista[pos]:>7.2f}')
print('*' * 30)