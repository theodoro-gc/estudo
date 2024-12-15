from ex113 import moedas
p = float(input('Digite o preço:  '))
print(f'A metade de RS{p} é {moedas.metade(p)}')
print(f'O dobro de RS{p} é {moedas.dobro(p)}')
print(f'Aumentando 10% temos RS{moedas.aumentar(p)}')
