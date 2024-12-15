def voto(IdadeDeNascimento):
    from datetime import date
    atual =date.today().year
    idade = atual - IdadeDeNascimento
    if idade < 16:
        return f'COM {idade} NÃO PODE VOTAR'
    elif 16 <= idade < 18 or idade > 65:
        return f'COM {idade} ANOS VOTO OPCIONAL'
    else:
        return f'COM {idade} VOTO OBRIGATORIO'






nasc = int(input('Em que ano você nasceu:  '))
print(voto(nasc))