nun = str(input('Digite sua expressão:  '))
pilha = []
for silaba in nun:
    if silaba == '(':
        pilha.append('(')
    elif silaba == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressao esta valida')
else:
    print('Sua expressao esta errada')