def idade(a):
    from datetime import datetime

    ano_atual = datetime.now().year
    idade = ano_atual - a

    if idade <= 15:
        return f'Você tem {idade} anos. Não pode votar.'

    elif 18 <= idade <= 59:
        return f'Você tem {idade} anos. Voto obrigatório.'

    else:
        return f'Você tem {idade} anos. Voto opcional.' 


# Programa princpal
txt = 'COM QUE IDADE POSSO VOTAR?'

print('=' * len(txt))
print(txt)
print('=' * len(txt), '\n')

nasc = int(input('Em que ano você nasceu? '))

print(idade(nasc))
