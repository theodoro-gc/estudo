somador = 0
caunt = 0
for c in range(1 , 501,2):
             if c % 3 == 0:
                somador += c
                caunt += 1
                print('a soma dos {} valores da {}'.format(caunt,somador ))

