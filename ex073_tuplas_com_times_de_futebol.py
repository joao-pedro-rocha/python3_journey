brasileirao = ('Cuiabá', 'Juventude', 'Bahia', 'Santos',
               'São Paulo', 'Fluminense', 'Atlético-MG', 'Fortaleza',
               'Flamengo', 'Palmeiras', 'Ceará SC', 'Grêmio',
               'Corinthians', 'Atlético-GO', 'Chapecoense', 'Bragantino',
               'Athletico-PR', 'América-MG', 'Internacional', 'Sport Recife')

print('=-' * 15)
print('LISTA DE TIMES DO BRASILEIRAO: ', end = '')
print(brasileirao)

print('')

print('=-' * 15)
print('OS 5 PRIMEIROS SAO: ', end = '')
print(brasileirao[:5])

print('')

print('=-' * 15)
print('OS 4 ULTIMOS SAO: ', end = '')
print(brasileirao[-4:])

print('')

print('=-' * 15)
print('LISTA DOS TIMES EM ORDEM ALFABETICA: ', end = '')
print(sorted(brasileirao))

print('')

print('=-' * 15)
print(f'A CHAPECOENSE ESTA NA {brasileirao.index("Chapecoense")}ª POSICAO')

