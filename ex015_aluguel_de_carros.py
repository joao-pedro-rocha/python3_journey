dias = int(input('Quantos dias de aluguel? '))
km = float(input('Quantos quilômetros rodados? '))
aluguel = (dias * 60) + (km * 0.15)

print('O valor do aluguel é R${:.2f}.'.format(aluguel))
