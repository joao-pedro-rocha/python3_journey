km = float(input('Sua viagem é de quantos quilometros? '))

'''if km < 201:
    print('O valor da sua passagem sera de R${:.2f}.'.format(km * 0.5))
else:
    print('Sua passagem custara R${:.2f}'.format(km * 0.45))'''

#OUTRA FORMA DE FAZER

valor = km * 0.50 if km <= 200 else km * 0.45

print('Sua passagem custara R${:.2f}.'.format(valor))

print('Tenha uma boa viagem!') 
