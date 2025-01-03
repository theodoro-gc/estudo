def aumentar(preco=0, taxa=0, formato=False):
    res = preco +(preco * taxa/100)
    return res if formato is False else moeda(res)


def diminuir(preco = 0 , taxa = 0,formato=False):
    res = preco - (preco * taxa/100)
    return res if formato is False else moeda(res)


def dobro(preco,formato=False):
    res = preco * 2
    return res if not formato else moeda(res)


def metade(preco,formato=False):
    res = preco / 2
    return res if not formato else moeda(res)


def moeda(preco = 0, moeda = 'R$'):
    return f'{moeda}{preco:.2f}'.replace('.',',')

def resumo(preco=0, taxa=10, taxar=5):
    print('--' * 30)
    print('RESUMO DO VALOR'.center(55))
    print('--' * 30)
    print(f'preço analizando: \t{moeda(preco)}')
    print(f'Dobro do preço: \t{dobro(preco, True)}')
    print(f'A metade o preço: \t{metade(preco, True)}')
    print(f'{taxa}% de aumento: \t{aumentar(preco, taxa, True)}')
    print(f'{taxa}% de redução: \t  {diminuir(preco, taxar, True)}')
    print('--' * 30)