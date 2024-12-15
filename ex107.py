def fatorial(n, show = False):
    """Calcula o fatorial de um numero
    :param n: O numero a ser calculado.
    :param show: (Opiconal) mostra ou não a conta.
    :return: O valor do fatorial de um numero n."""
    resultado = 1
    for i in range(1, numero + 1):
        resultado *= i
    return resultado


numero = 5
resultado = fatorial(numero)
print("O fatorial de", numero, "é", resultado)
help(fatorial)